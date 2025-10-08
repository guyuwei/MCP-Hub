# 🚀 MCP Hub 快速参考卡片

## 📥 安装和启动

### 一键安装
```bash
# Linux/macOS
sudo ./one_click.sh

# Windows
install.bat → one_click.bat

# Docker
sudo ./docker_start.sh
```

### 直接启动模式
```bash
sudo ./start_ai.sh        # AI研究模式
sudo ./start_notes.sh     # 笔记模式
sudo ./start_writing.sh   # 写作模式
sudo ./start_engineering.sh  # 工程模式
sudo ./start_experiment.sh   # 实验模式
```

---

## 🎯 五种工作模式

| 模式 | 命令 | 适合人群 | 主要工具 |
|------|------|----------|----------|
| 🔬 **AI研究** | `--mode=ai` | 数据科学家、AI研究员 | Ray + Dask + OpenAI |
| 📚 **笔记** | `--mode=notes` | 学生、研究人员 | Obsidian + Zotero |
| 💬 **写作** | `--mode=writing` | 作家、内容创作者 | LangChain + LangGraph |
| 🧪 **工程** | `--mode=engineering` | 工程师、设计师 | Simulink + Python |
| 🧭 **实验** | `--mode=experiment` | 项目经理、开发者 | FastAPI + GitHub + Shortcuts |

---

## 💻 交互式命令

### 基本命令
```
help                    # 显示帮助
status                  # 查看状态
tools                   # 列出工具
quit                    # 退出程序
```

### 工具管理
```
connect <工具名>         # 连接工具
disconnect <工具名>      # 断开工具
restart                 # 重启Hub
```

### 示例操作
```
MCP> status             # 查看当前状态
MCP> tools              # 查看所有工具
MCP> connect ray        # 连接Ray工具
MCP> quit               # 退出程序
```

---

## 🔧 环境配置

### 设置API密钥
```bash
sudo ./setup_env.sh
```

### 环境变量
```bash
export OPENAI_API_KEY="your-key"           # AI模式
export OBSIDIAN_VAULT_PATH="/path/to/vault" # 笔记模式
export GITHUB_TOKEN="your-token"           # 实验模式
```

---

## 🆘 常见问题

### 权限问题
```bash
chmod +x *.sh           # 添加执行权限
sudo ./one_click.sh     # 使用sudo运行
```

### 依赖问题
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 连接问题
```bash
MCP> restart            # 重启Hub
cat mcp_hub.log         # 查看日志
```

---

## 📚 文档资源

- [完整功能指南](COMPLETE_GUIDE.md) - 详细说明
- [使用指南](USAGE_GUIDE.md) - 快速上手
- [GitHub Issues](https://github.com/guyuwei/MCP-Hub/issues) - 问题反馈

---

## 💡 使用技巧

1. **新手建议**：从笔记模式开始
2. **定期检查**：使用 `status` 命令
3. **查看日志**：`cat mcp_hub.log`
4. **备份配置**：保存 `config.json`

**🎉 开始你的智能工作之旅！**
