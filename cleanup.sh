#!/bin/bash
# MCP Hub 清理脚本
# =================
# 清理所有过程文件和临时文件

echo "🧹 MCP Hub 清理脚本"
echo "=================="

# 清理Python缓存
echo "🔍 清理Python缓存文件..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
find . -name "*.pyo" -delete 2>/dev/null || true

# 清理虚拟环境
echo "🔍 清理虚拟环境..."
rm -rf venv/ 2>/dev/null || true
rm -rf .venv/ 2>/dev/null || true
rm -rf env/ 2>/dev/null || true

# 清理日志文件
echo "🔍 清理日志文件..."
rm -f *.log 2>/dev/null || true
rm -f logs/*.log 2>/dev/null || true

# 清理临时文件
echo "🔍 清理临时文件..."
rm -f *.tmp 2>/dev/null || true
rm -f *.temp 2>/dev/null || true
rm -rf temp/ 2>/dev/null || true
rm -rf tmp/ 2>/dev/null || true

# 清理系统文件
echo "🔍 清理系统文件..."
find . -name ".DS_Store" -delete 2>/dev/null || true
find . -name "Thumbs.db" -delete 2>/dev/null || true

# 清理IDE文件
echo "🔍 清理IDE文件..."
rm -rf .vscode/ 2>/dev/null || true
rm -rf .idea/ 2>/dev/null || true
rm -f *.swp 2>/dev/null || true
rm -f *.swo 2>/dev/null || true

# 清理构建文件
echo "🔍 清理构建文件..."
rm -rf build/ 2>/dev/null || true
rm -rf dist/ 2>/dev/null || true
rm -rf *.egg-info/ 2>/dev/null || true

echo "✅ 清理完成！"
echo ""
echo "📊 当前项目状态:"
echo "总文件数: $(find . -type f | grep -v ".git" | wc -l)"
echo "项目大小: $(du -sh . | cut -f1)"
