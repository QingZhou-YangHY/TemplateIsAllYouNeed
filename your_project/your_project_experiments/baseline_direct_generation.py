"""
Baseline实验脚本 - yourbaseline
对比实验: yourbaseline
"""

import os
import json
import argparse
import time
from datetime import datetime
from tqdm import tqdm
import torch
import transformers

transformers.utils.logging.disable_progress_bar()

from model_configs import get_model_path


def format_prompt_alpaca(instruction, input_text=""):
    """格式化Alpaca数据集的prompt"""
    if input_text:
        return f"### Instruction:\n{instruction}\n\n### Input:\n{input_text}\n\n### Response:\n"
    else:
        return f"### Instruction:\n{instruction}\n\n### Response:\n"


def main():
    parser = argparse.ArgumentParser(description="Baseline: Baseline Direct Generation Experiment")
    
    # 模型参数
    parser.add_argument("--model", type=str, required=True,
                       choices=["qwen_math", "qwen", "phi", "qwen25_7b", "qwen3_8b_base",
                               "qwen3_14b", "qwen25_7b_instruct", "qwen3_8b_instruct"],
                       help="Model name")
    parser.add_argument("--dataset", type=str, required=True,
                       choices=["math", "gpqa", "he", "alpaca"],
                       help="Dataset name")
    
    # 生成参数
    parser.add_argument("--generation_mode", type=str, default="greedy",
                       choices=["greedy", "beam_search", "sampling", "nucleus"],
                       help="Generation mode")
    parser.add_argument("--temperature", type=float, default=0.7,
                       help="Sampling temperature")
    parser.add_argument("--top_p", type=float, default=0.9,
                       help="Top-p for nucleus sampling")
    parser.add_argument("--num_beams", type=int, default=5,
                       help="Number of beams for beam search")
    parser.add_argument("--max_new_tokens", type=int, default=3072,
                       help="Maximum new tokens to generate")
    
    # 数据和保存参数
    parser.add_argument("--batch_idx", type=int, default=0,
                       help="Batch index for parallel processing")
    parser.add_argument("--batch_size", type=int, default=None,
                       help="Batch size (default: None = use full dataset)")
    parser.add_argument("--output_dir", type=str, default="results/baseline_direct",
                       help="Output directory")
    parser.add_argument("--seed", type=int, default=0,
                       help="Random seed")
    
    args = parser.parse_args()
    
    # 设置随机种子
    torch.manual_seed(args.seed)
    
    # 记录实验开始时间
    experiment_start_time = time.time()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print("=" * 80)
    print(f"Baseline: Direct Generation - {args.dataset.upper()}")
    print("=" * 80)
    print(f"Model: {args.model}")
    print(f"Dataset: {args.dataset}")
    print(f"Generation mode: {args.generation_mode}")
    if args.generation_mode == "sampling" or args.generation_mode == "nucleus":
        print(f"Temperature: {args.temperature}")
    if args.generation_mode == "nucleus":
        print(f"Top-p: {args.top_p}")
    if args.generation_mode == "beam_search":
        print(f"Num beams: {args.num_beams}")
    print("=" * 80)
    
    # 获取模型路径
    model_path = get_model_path(args.model)
    
    # 加载数据集
    data_files = {
        "math": "data/MATH500.json",
        "gpqa": "data/GPQA.jsonl",
        "he": "data/HumanEval.jsonl",
        "alpaca": "data/ALPACA.json"
    }
    data_file = data_files[args.dataset]
    
    with open(data_file, 'r', encoding='utf-8') as f:
        if data_file.endswith('.jsonl'):
            dataset = [json.loads(line) for line in f if line.strip()]
        else:
            dataset = json.load(f)
    
    print(f"Dataset loaded: {len(dataset)} examples")
    
    # 确定要处理的数据范围
    # 如果没有指定batch_size，使用整个数据集
    if args.batch_size is None:
        args.batch_size = len(dataset)
        print(f"Using full dataset: {args.batch_size} examples")
    
    start_idx = args.batch_idx * args.batch_size
    end_idx = min((args.batch_idx + 1) * args.batch_size, len(dataset))
    batch_dataset = dataset[start_idx:end_idx]
    
    print(f"Processing examples {start_idx} to {end_idx-1} (total: {len(batch_dataset)})")
    
    # 加载模型
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_path,
        trust_remote_code=True
    )
    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True
    )
    
    print("Model loaded")
    
    # 准备输出目录
    os.makedirs(args.output_dir, exist_ok=True)
    
    # 结果列表
    results = []
    
    # 处理每个问题
    for idx, item in enumerate(tqdm(batch_dataset, desc=f"{args.dataset} examples")):
        problem_start_time = time.time()
        
        # 根据数据集类型格式化prompt
        if args.dataset == "alpaca":
            instruction = item.get("instruction", "")
            input_text = item.get("input", "")
            prompt = format_prompt_alpaca(instruction, input_text)
        else:
            prompt = item.get("problem", item.get("prompt", ""))
        
        print(f"\n{'=' * 80}")
        print(f"Example {start_idx + idx + 1}/{len(dataset)}")
        print(f"Prompt: {prompt[:100]}...")
        print("=" * 80)
        
        # 编码输入
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        # 配置生成参数
        gen_kwargs = {
            "max_new_tokens": args.max_new_tokens,
            "pad_token_id": tokenizer.eos_token_id,
        }
        
        if args.generation_mode == "greedy":
            gen_kwargs["do_sample"] = False
        elif args.generation_mode == "beam_search":
            gen_kwargs["num_beams"] = args.num_beams
            gen_kwargs["do_sample"] = False
        elif args.generation_mode == "sampling":
            gen_kwargs["do_sample"] = True
            gen_kwargs["temperature"] = args.temperature
        elif args.generation_mode == "nucleus":
            gen_kwargs["do_sample"] = True
            gen_kwargs["temperature"] = args.temperature
            gen_kwargs["top_p"] = args.top_p
        
        # 生成
        with torch.no_grad():
            outputs = model.generate(**inputs, **gen_kwargs)
        
        # 解码
        response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
        
        problem_time = time.time() - problem_start_time
        
        print(f"\n生成的响应长度: {len(response)} chars")
        print(f"问题耗时: {problem_time:.2f}秒")
        
        # 保存结果
        result = {
            "example_idx": start_idx + idx,
            "prompt": prompt[:200],
            "response": response,
            "time_seconds": problem_time,
            "generation_mode": args.generation_mode,
        }
        
        if args.dataset != "alpaca":
            result["ground_truth"] = item.get("solution", item.get("answer", ""))
        
        results.append(result)
    
    # 保存结果
    experiment_time = time.time() - experiment_start_time
    
    output_basename = f"baseline-direct-{args.dataset}-{args.model}-{args.generation_mode}-batch{args.batch_idx}-{timestamp}"
    
    # 保存CSV结果
    import pandas as pd
    df = pd.DataFrame(results)
    csv_path = os.path.join(args.output_dir, f"{output_basename}.csv")
    df.to_csv(csv_path, index=False)
    print(f"\n结果已保存到: {csv_path}")
    
    # 保存详细JSON日志
    json_path = os.path.join(args.output_dir, f"{output_basename}_detailed.json")
    with open(json_path, 'w') as f:
        json.dump({
            "config": vars(args),
            "timestamp": timestamp,
            "experiment_time_seconds": experiment_time,
            "results": results,
        }, f, indent=2)
    print(f"详细日志已保存到: {json_path}")
    
    # 打印统计
    print("\n" + "=" * 80)
    print("实验统计")
    print("=" * 80)
    print(f"总样本数: {len(results)}")
    print(f"总耗时: {experiment_time:.2f}秒 ({experiment_time/60:.2f}分钟)")
    print(f"平均每个样本: {experiment_time/len(results):.2f}秒")
    print("=" * 80)


if __name__ == "__main__":
    main()
