#!/bin/bash
# MCP Hub 一键启动脚本
# ===================
# 自动检测环境，安装依赖，启动MCP Hub

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                    🚀 MCP Hub 一键启动                       ║"
echo "║                    简单易用，一键搞定！                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# 检查是否已安装
if [ ! -d "venv" ] || [ ! -f "start_mcp.sh" ]; then
    echo -e "${YELLOW}🔧 检测到首次使用，正在自动安装...${NC}"
    ./install.sh
    echo -e "${GREEN}✅ 安装完成！${NC}"
fi

# 显示模式选择
echo -e "\n${PURPLE}🎯 请选择MCP Hub模式:${NC}"
echo "1) 🔬 AI研究模式 (Ray + Dask + OpenAI)"
echo "2) 📚 笔记模式 (Obsidian + Zotero)"
echo "3) 💬 写作模式 (LangChain + LangGraph)"
echo "4) 🧪 工程模式 (Simulink + Python)"
echo "5) 🧭 实验模式 (FastAPI + GitHub)"
echo "6) 🎭 演示模式 (查看所有模式)"
echo "7) ❓ 帮助信息"

read -p "请输入选择 (1-7): " choice

case $choice in
    1)
        echo -e "${GREEN}🚀 启动AI研究模式...${NC}"
        ./start_ai.sh
        ;;
    2)
        echo -e "${GREEN}🚀 启动笔记模式...${NC}"
        ./start_notes.sh
        ;;
    3)
        echo -e "${GREEN}🚀 启动写作模式...${NC}"
        ./start_writing.sh
        ;;
    4)
        echo -e "${GREEN}🚀 启动工程模式...${NC}"
        ./start_engineering.sh
        ;;
    5)
        echo -e "${GREEN}🚀 启动实验模式...${NC}"
        ./start_experiment.sh
        ;;
    6)
        echo -e "${GREEN}🚀 启动演示模式...${NC}"
        source venv/bin/activate
        python demo.py
        ;;
    7)
        echo -e "${GREEN}📖 显示帮助信息...${NC}"
        source venv/bin/activate
        python mcp_hub.py --help
        ;;
    *)
        echo -e "${RED}❌ 无效选择，启动默认AI模式...${NC}"
        ./start_ai.sh
        ;;
esac
