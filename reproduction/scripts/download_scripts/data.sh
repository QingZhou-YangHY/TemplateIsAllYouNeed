# 这里以下载 GPQA 数据集的 diamond 子集为例
#!/bin/bash

# 1. 定义参数
DATASET_ID="Idavidrein/gpqa"
CONFIG_NAME="diamond"  # 明确指定只下载 'diamond' 子集
TARGET_DIR="/home/your_username/reproduction_project/data" # 建议为特定子集设置专属文件夹

# 2. 确保目标目录存在
mkdir -p "${TARGET_DIR}"

echo "Starting download of GPQA dataset: ${DATASET_ID} (${CONFIG_NAME} subset)..."

# 3. 执行下载命令
# 使用 --config-name 确保只下载 diamond 配置所需的文件
huggingface-cli download \
    "${DATASET_ID}" \
    --config-name "${CONFIG_NAME}" \
    --local-dir "${TARGET_DIR}" \
    --local-dir-use-symlinks False \
    --resume-download 

echo "Download finished for GPQA Diamond subset."
echo "Files saved to: ${TARGET_DIR}"