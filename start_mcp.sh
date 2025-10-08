#!/bin/bash
# MCP Hub 启动脚本

# 激活虚拟环境
source venv/bin/activate

# 启动MCP Hub
python mcp_hub.py "$@"
