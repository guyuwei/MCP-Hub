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
