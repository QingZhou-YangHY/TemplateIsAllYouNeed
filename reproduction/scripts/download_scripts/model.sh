# 这里以下载 Qwen2.5-Math-7B 模型为例
# 1. 定义模型和本地保存路径
MODEL_NAME="Qwen/Qwen2.5-Math-7B"
LOCAL_SAVE_PATH="/data/your_username/reproduction_project/models/Qwen/Qwen2.5-Math-7B" # 您希望保存的本地目录

# 2. 执行下载命令
huggingface-cli download \
    --local-dir $LOCAL_SAVE_PATH \
    --local-dir-use-symlinks False \
    $MODEL_NAME