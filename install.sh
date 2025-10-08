#!/bin/bash
# MCP Hub 一键安装脚本
# =====================
# 自动安装所有依赖并配置环境

set -e  # 遇到错误立即退出

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_message() {
    echo -e "${2}${1}${NC}"
}

print_header() {
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    🚀 MCP Hub 自动安装器                      ║"
    echo "║              Standalone Model Context Protocol              ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_step() {
    echo -e "\n${CYAN}🔧 步骤 $1: $2${NC}"
    echo "────────────────────────────────────────────────────────────"
}

# 检查系统要求
check_requirements() {
    print_step "1" "检查系统要求"
    
    # 检查Python
    if ! command -v python3 &> /dev/null; then
        print_message "❌ Python3 未安装。请先安装 Python 3.8+" "$RED"
        exit 1
    fi
    
    # 检查Python版本
    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    REQUIRED_VERSION="3.8"
    
    if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
        print_message "❌ Python 版本过低: $PYTHON_VERSION (需要 3.8+)" "$RED"
        exit 1
    fi
    
    print_message "✅ Python $PYTHON_VERSION 已安装" "$GREEN"
    
    # 检查pip
    if ! command -v pip3 &> /dev/null; then
        print_message "❌ pip3 未安装" "$RED"
        exit 1
    fi
    
    print_message "✅ pip3 已安装" "$GREEN"
}

# 创建虚拟环境
create_venv() {
    print_step "2" "创建Python虚拟环境"
    
    if [ ! -d "venv" ]; then
        print_message "📦 创建虚拟环境..." "$YELLOW"
        python3 -m venv venv
        print_message "✅ 虚拟环境创建成功" "$GREEN"
    else
        print_message "✅ 虚拟环境已存在" "$GREEN"
    fi
}

# 激活虚拟环境并安装依赖
install_dependencies() {
    print_step "3" "安装依赖包"
    
    print_message "🔄 激活虚拟环境..." "$YELLOW"
    source venv/bin/activate
    
    print_message "📦 升级pip..." "$YELLOW"
    pip install --upgrade pip
    
    print_message "📦 安装项目依赖..." "$YELLOW"
    pip install -r requirements.txt
    
    print_message "✅ 依赖安装完成" "$GREEN"
}

# 创建启动脚本
create_launcher() {
    print_step "4" "创建启动脚本"
    
    cat > start_mcp.sh << 'EOF'
#!/bin/bash
# MCP Hub 启动脚本

# 激活虚拟环境
source venv/bin/activate

# 启动MCP Hub
python mcp_hub.py "$@"
EOF
    
    chmod +x start_mcp.sh
    print_message "✅ 启动脚本创建成功" "$GREEN"
}

# 创建快速启动脚本
create_quick_launchers() {
    print_step "5" "创建快速启动脚本"
    
    # AI模式
    cat > start_ai.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python mcp_hub.py --mode=ai
EOF
    
    # 笔记模式
    cat > start_notes.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python mcp_hub.py --mode=notes
EOF
    
    # 写作模式
    cat > start_writing.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python mcp_hub.py --mode=writing
EOF
    
    # 工程模式
    cat > start_engineering.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python mcp_hub.py --mode=engineering
EOF
    
    # 实验模式
    cat > start_experiment.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python mcp_hub.py --mode=experiment
EOF
    
    chmod +x start_*.sh
    print_message "✅ 快速启动脚本创建成功" "$GREEN"
}

# 创建环境配置脚本
create_env_setup() {
    print_step "6" "创建环境配置脚本"
    
    cat > setup_env.sh << 'EOF'
#!/bin/bash
# 环境变量配置脚本

echo "🔧 MCP Hub 环境配置"
echo "=================="
echo ""

# OpenAI API Key
read -p "请输入 OpenAI API Key (可选): " OPENAI_KEY
if [ ! -z "$OPENAI_KEY" ]; then
    echo "export OPENAI_API_KEY=\"$OPENAI_KEY\"" >> ~/.bashrc
    echo "export OPENAI_API_KEY=\"$OPENAI_KEY\"" >> ~/.zshrc
    echo "✅ OpenAI API Key 已配置"
fi

# Obsidian Vault Path
read -p "请输入 Obsidian 仓库路径 (可选): " OBSIDIAN_PATH
if [ ! -z "$OBSIDIAN_PATH" ]; then
    echo "export OBSIDIAN_VAULT_PATH=\"$OBSIDIAN_PATH\"" >> ~/.bashrc
    echo "export OBSIDIAN_VAULT_PATH=\"$OBSIDIAN_PATH\"" >> ~/.zshrc
    echo "✅ Obsidian 路径已配置"
fi

# GitHub Token
read -p "请输入 GitHub Token (可选): " GITHUB_TOKEN
if [ ! -z "$GITHUB_TOKEN" ]; then
    echo "export GITHUB_TOKEN=\"$GITHUB_TOKEN\"" >> ~/.bashrc
    echo "export GITHUB_TOKEN=\"$GITHUB_TOKEN\"" >> ~/.zshrc
    echo "✅ GitHub Token 已配置"
fi

echo ""
echo "🎉 环境配置完成！请重新启动终端或运行:"
echo "source ~/.bashrc  # 或 source ~/.zshrc"
EOF
    
    chmod +x setup_env.sh
    print_message "✅ 环境配置脚本创建成功" "$GREEN"
}

# 显示使用说明
show_usage() {
    print_step "7" "安装完成！"
    
    echo -e "${GREEN}"
    echo "🎉 MCP Hub 安装成功！"
    echo ""
    echo "📖 使用方法:"
    echo "  ./start_mcp.sh --mode=ai          # 启动AI研究模式"
    echo "  ./start_mcp.sh --mode=notes       # 启动笔记模式"
    echo "  ./start_mcp.sh --mode=writing     # 启动写作模式"
    echo "  ./start_mcp.sh --help             # 查看帮助"
    echo ""
    echo "⚡ 快速启动:"
    echo "  ./start_ai.sh                     # 直接启动AI模式"
    echo "  ./start_notes.sh                  # 直接启动笔记模式"
    echo "  ./start_writing.sh                # 直接启动写作模式"
    echo ""
    echo "🔧 环境配置:"
    echo "  ./setup_env.sh                    # 配置API密钥"
    echo ""
    echo "📚 更多信息:"
    echo "  cat README.md                     # 查看详细文档"
    echo -e "${NC}"
}

# 主函数
main() {
    print_header
    
    check_requirements
    create_venv
    install_dependencies
    create_launcher
    create_quick_launchers
    create_env_setup
    show_usage
}

# 运行主函数
main "$@"
