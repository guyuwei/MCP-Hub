# MCP Hub Docker 镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 创建启动脚本
RUN echo '#!/bin/bash\npython mcp_hub.py "$@"' > /usr/local/bin/start-mcp && \
    chmod +x /usr/local/bin/start-mcp

# 暴露端口（如果需要）
EXPOSE 8000

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 默认启动命令
CMD ["python", "mcp_hub.py", "--mode=ai"]
