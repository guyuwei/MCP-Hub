# 🚀 MCP Hub - 使用指南

## 🎯 一句话使用

**下载项目 → 运行脚本 → 选择模式 → 开始使用！**

## 📥 第一步：下载项目

```bash
# 方法1：Git克隆
git clone https://github.com/guyuwei/MCP-Hub.git
cd MCP-Hub

# 方法2：直接下载ZIP
# 访问 https://github.com/guyuwei/MCP-Hub
# 点击 "Code" → "Download ZIP"
# 解压后进入文件夹
```

## 🚀 第二步：一键启动

### Linux/macOS 用户

```bash
# 打开终端，输入以下命令：
sudo ./one_click.sh
```

### Windows 用户

```batch
# 双击运行
install.bat
# 然后双击运行
one_click.bat
```

## 🎯 第三步：选择模式

运行后会看到菜单：

```
🎯 请选择MCP Hub模式:
1) 🔬 AI研究模式 (Ray + Dask + OpenAI)
2) 📚 笔记模式 (Obsidian + Zotero)  
3) 💬 写作模式 (LangChain + LangGraph)
4) 🧪 工程模式 (Simulink + Python)
5) 🧭 实验模式 (FastAPI + GitHub)
6) 🎭 演示模式 (查看所有模式)
7) ❓ 帮助信息
```

**输入数字 1-7，按回车即可！**

## ⚡ 快速启动（安装后）

安装完成后，你可以直接运行：

### Linux/macOS

```bash
sudo ./start_ai.sh        # AI研究模式
sudo ./start_notes.sh     # 笔记模式
sudo ./start_writing.sh   # 写作模式
```

### Windows

```batch
start_ai.bat         # AI研究模式
start_notes.bat      # 笔记模式
start_writing.bat    # 写作模式
```

## 🔧 环境配置（可选）

如果需要使用API功能，运行：

```bash
# Linux/macOS
sudo ./setup_env.sh

# Windows
setup_env.bat
```

然后按提示输入：

- OpenAI API Key（AI模式需要）
- Obsidian 仓库路径（笔记模式需要）
- GitHub Token（实验模式需要）

## 🆘 遇到问题？

1. **Python未安装**：访问 https://python.org 下载安装
2. **权限问题**：运行 `chmod +x *.sh`（Linux/macOS）
3. **依赖安装失败**：检查网络连接，或使用国内镜像
4. **其他问题**：查看 `mcp_hub.log` 日志文件


## 📚 更多文档

- [完整功能指南](COMPLETE_GUIDE.md) - 详细的功能说明和使用教程
- [快速参考卡片](QUICK_REFERENCE.md) - 常用命令和操作速查
- [GitHub Issues](https://github.com/guyuwei/MCP-Hub/issues) - 问题反馈和讨论

**有问题？** 访问 [GitHub Issues](https://github.com/guyuwei/MCP-Hub/issues) 提问
