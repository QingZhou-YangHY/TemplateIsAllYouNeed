#!/bin/bash

# Baseline实验运行脚本
# 对比三种关键的Baseline方法

# 超参数设置
BATCH_IDX=0
OUTPUT_DIR_BASE="results/results_1/baseline"
MAX_NEW_TOKENS=3072

echo "======================================================================"
echo "Baseline 实验套件"
echo "======================================================================"
echo "将运行以下三类Baseline实验："
echo "  1. xxx"
echo "  2. xxx"
echo "  3. xxx"
echo "======================================================================"
echo ""

TOTAL_START_TIME=$(date +%s)

# ============================================================================
# Baseline 1: Base模型 (Qwen2.5-7B) 直接生成 - Greedy
# ============================================================================
echo ""
echo "【Baseline 1】Base模型直接生成 (Greedy Decoding)"
echo "模型: qwen25_7b"
echo "======================================================================"

OUTPUT_DIR="${OUTPUT_DIR_BASE}/qwen25_7b_direct_greedy"
mkdir -p ${OUTPUT_DIR}/logs

DATASETS=("math" "gpqa" "he" "alpaca")
pids_b1=()

for dataset in "${DATASETS[@]}"; do
    gpu=$((${#pids_b1[@]} % 4))
    log_file="${OUTPUT_DIR}/logs/${dataset}-qwen25_7b-greedy-$(date +%Y%m%d_%H%M%S).log"
    
    echo "  GPU ${gpu}: ${dataset} (qwen25_7b, greedy)"
    
    CUDA_VISIBLE_DEVICES=${gpu} python -u baseline_direct_generation.py \
        --model qwen25_7b \
        --dataset ${dataset} \
        --generation_mode greedy \
        --max_new_tokens ${MAX_NEW_TOKENS} \
        --batch_idx ${BATCH_IDX} \
        --output_dir ${OUTPUT_DIR} \
        > ${log_file} 2>&1 &
    
    pids_b1+=($!)
done

echo "等待 Baseline 1 完成..."
for pid in "${pids_b1[@]}"; do
    wait $pid
done
echo "✓ Baseline 1 完成"

# ============================================================================
# Baseline 2: 
# ============================================================================
echo ""
echo "【Baseline 2】"
echo "模型: qwen3_14b"
echo "======================================================================"

OUTPUT_DIR="${OUTPUT_DIR_BASE}/qwen3_14b_direct_greedy"
mkdir -p ${OUTPUT_DIR}/logs

pids_b2=()

for dataset in "${DATASETS[@]}"; do
    gpu=$((${#pids_b2[@]} % 4))
    log_file="${OUTPUT_DIR}/logs/${dataset}-qwen3_14b-greedy-$(date +%Y%m%d_%H%M%S).log"
    
    echo "  GPU ${gpu}: ${dataset} (qwen3_14b, greedy)"
    
    CUDA_VISIBLE_DEVICES=${gpu} python -u baseline_direct_generation.py \
        --model qwen3_14b \
        --dataset ${dataset} \
        --generation_mode greedy \
        --max_new_tokens ${MAX_NEW_TOKENS} \
        --batch_idx ${BATCH_IDX} \
        --output_dir ${OUTPUT_DIR} \
        > ${log_file} 2>&1 &
    
    pids_b2+=($!)
done

echo "等待 Baseline 2 完成..."
for pid in "${pids_b2[@]}"; do
    wait $pid
done
echo "✓ Baseline 2 完成"

# ============================================================================
# Baseline 3
# ============================================================================
echo ""
echo "【Baseline 3】"
echo "模型: qwen25_7b"
echo "======================================================================"

OUTPUT_DIR="${OUTPUT_DIR_BASE}/qwen25_7b_direct_sampling"
mkdir -p ${OUTPUT_DIR}/logs

pids_b3=()

for dataset in "${DATASETS[@]}"; do
    gpu=$((${#pids_b3[@]} % 4))
    log_file="${OUTPUT_DIR}/logs/${dataset}-qwen25_7b-sampling-$(date +%Y%m%d_%H%M%S).log"
    
    echo "  GPU ${gpu}: ${dataset} (qwen25_7b, sampling)"
    
    CUDA_VISIBLE_DEVICES=${gpu} python -u baseline_direct_generation.py \
        --model qwen25_7b \
        --dataset ${dataset} \
        --generation_mode sampling \
        --temperature 0.7 \
        --max_new_tokens ${MAX_NEW_TOKENS} \
        --batch_idx ${BATCH_IDX} \
        --output_dir ${OUTPUT_DIR} \
        > ${log_file} 2>&1 &
    
    pids_b3+=($!)
done

echo "等待 Baseline 3 完成..."
for pid in "${pids_b3[@]}"; do
    wait $pid
done
echo "✓ Baseline 3 完成"

# ============================================================================
# 完成
# ============================================================================

TOTAL_END_TIME=$(date +%s)
TOTAL_TIME=$((TOTAL_END_TIME - TOTAL_START_TIME))
TOTAL_HOURS=$((TOTAL_TIME / 3600))
TOTAL_MINUTES=$(((TOTAL_TIME % 3600) / 60))

echo ""
echo "======================================================================"
echo "所有 Baseline 实验完成！"
echo "======================================================================"
echo "总耗时: ${TOTAL_HOURS}小时 ${TOTAL_MINUTES}分钟"
echo ""
echo "结果保存在:"
echo "  Baseline 1: ${OUTPUT_DIR_BASE}/qwen25_7b_direct_greedy/"
echo "  Baseline 2: ${OUTPUT_DIR_BASE}/qwen3_14b_direct_greedy/"
echo "  Baseline 3: ${OUTPUT_DIR_BASE}/qwen25_7b_direct_sampling/"
echo "======================================================================"
