import pandas as pd
import json
import argparse
from pathlib import Path

def csv_to_jsonl(csv_filepaths: list, output_filepath: str):
    """
    将一个或多个 CSV 文件合并并转换为单个 JSONL 文件。

    Args:
        csv_filepaths: 包含输入 CSV 文件路径的列表。
        output_filepath: 最终生成的 JSONL 文件的路径和名称。
    """
    all_data = []
    
    print(f"Starting conversion process...")

    # 1. 读取和合并所有 CSV 文件
    for csv_path in csv_filepaths:
        try:
            print(f"Reading CSV: {csv_path}")
            df = pd.read_csv(csv_path)
            # 将 DataFrame 的每一行转换为一个字典，并添加到列表中
            all_data.extend(df.to_dict('records'))
        except FileNotFoundError:
            print(f"Warning: CSV file not found at {csv_path}. Skipping.")
        except Exception as e:
            print(f"Error reading {csv_path}: {e}. Skipping.")

    if not all_data:
        print("No data was successfully loaded. Exiting.")
        return

    # 2. 确保输出目录存在
    Path(output_filepath).parent.mkdir(parents=True, exist_ok=True)

    # 3. 写入 JSONL 文件
    print(f"Writing {len(all_data)} records to JSONL file: {output_filepath}")
    with open(output_filepath, 'w', encoding='utf-8') as fout:
        for record in all_data:
            # 将字典转换为 JSON 字符串，并写入一行
            fout.write(json.dumps(record) + "\n")
            
    print("Conversion completed successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV files to a single JSONL file.")
    parser.add_argument(
        "input_csv_files", 
        type=str, 
        nargs='+', # 接受一个或多个 CSV 文件作为输入
        help="One or more paths to input CSV files (e.g., 'results/std_*.csv')."
    )
    parser.add_argument(
        "--output", 
        type=str, 
        default="combined_output.jsonl", 
        help="Path and filename for the output JSONL file (default: combined_output.jsonl)."
    )
    args = parser.parse_args()
    
    # 调用转换函数
    csv_to_jsonl(args.input_csv_files, args.output)