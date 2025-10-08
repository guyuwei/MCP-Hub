#!/bin/bash
# MCP Hub Docker 一键启动脚本
# =============================

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                🐳 MCP Hub Docker 一键启动                    ║"
echo "║                    容器化部署，简单易用！                     ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker未安装，请先安装Docker${NC}"
    echo "安装指南: https://docs.docker.com/get-docker/"
    exit 1
fi

# 检查Docker Compose是否安装
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}❌ Docker Compose未安装，请先安装Docker Compose${NC}"
    echo "安装指南: https://docs.docker.com/compose/install/"
    exit 1
fi

echo -e "${GREEN}✅ Docker环境检查通过${NC}"

# 显示模式选择
echo -e "\n${PURPLE}🎯 请选择MCP Hub模式:${NC}"
echo "1) 🔬 AI研究模式 (Ray + Dask + OpenAI)"
echo "2) 📚 笔记模式 (Obsidian + Zotero)"
echo "3) 💬 写作模式 (LangChain + LangGraph)"
echo "4) 🧪 工程模式 (Simulink + Python)"
echo "5) 🧭 实验模式 (FastAPI + GitHub)"
echo "6) 🎭 演示模式 (查看所有模式)"
echo "7) 🏗️ 构建镜像"
echo "8) 🗑️ 清理容器"

read -p "请输入选择 (1-8): " choice

case $choice in
    1)
        echo -e "${GREEN}🚀 启动AI研究模式...${NC}"
        docker-compose --profile ai up mcp-ai
        ;;
    2)
        echo -e "${GREEN}🚀 启动笔记模式...${NC}"
        docker-compose --profile notes up mcp-notes
        ;;
    3)
        echo -e "${GREEN}🚀 启动写作模式...${NC}"
        docker-compose --profile writing up mcp-writing
        ;;
    4)
        echo -e "${GREEN}🚀 启动工程模式...${NC}"
        docker-compose up mcp-hub
        docker-compose exec mcp-hub python mcp_hub.py --mode=engineering
        ;;
    5)
        echo -e "${GREEN}🚀 启动实验模式...${NC}"
        docker-compose up mcp-hub
        docker-compose exec mcp-hub python mcp_hub.py --mode=experiment
        ;;
    6)
        echo -e "${GREEN}🚀 启动演示模式...${NC}"
        docker-compose up mcp-hub
        docker-compose exec mcp-hub python demo.py
        ;;
    7)
        echo -e "${GREEN}🏗️ 构建Docker镜像...${NC}"
        docker-compose build
        echo -e "${GREEN}✅ 镜像构建完成${NC}"
        ;;
    8)
        echo -e "${YELLOW}🗑️ 清理Docker容器和镜像...${NC}"
        docker-compose down
        docker system prune -f
        echo -e "${GREEN}✅ 清理完成${NC}"
        ;;
    *)
        echo -e "${RED}❌ 无效选择，启动默认AI模式...${NC}"
        docker-compose --profile ai up mcp-ai
        ;;
esac
