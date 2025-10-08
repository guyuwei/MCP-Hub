# MCP Hub - Standalone Model Context Protocol Orchestration

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-guyuwei%2FMCP--Hub-black.svg)](https://github.com/guyuwei/MCP-Hub)
[![MCP](https://img.shields.io/badge/MCP-Protocol-orange.svg)](https://modelcontextprotocol.io)

A standalone local MCP hub that connects and coordinates multiple Model Context Protocol tools. Works without Cursor - only requires Python and a terminal.

## 🚀 一键启动 (简单易用！)

### 🎯 最简单的方式

**Linux/macOS:**
```bash
# 下载项目后，直接运行：
./one_click.sh
```

**Windows:**
```batch
# 下载项目后，直接运行：
install.bat
# 然后运行：
one_click.bat
```

**Docker (任何系统):**
```bash
# 简单易用，一条命令搞定！
./docker_start.sh
```

### 🔧 传统安装方式

**Prerequisites:**
- Python 3.8 or higher
- pip (Python package installer)

**Installation:**

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/guyuwei/MCP-Hub.git
   cd MCP-Hub
   ```

2. **一键安装 (推荐)**
   ```bash
   # Linux/macOS
   ./install.sh
   
   # Windows
   install.bat
   ```

3. **手动安装**
   ```bash
   pip install -r requirements.txt
   python mcp_hub.py --mode=ai
   ```

## 🎯 Available Modes

| Mode | Command | Description | Tools |
|------|---------|-------------|-------|
| 🔬 **Data Science / AI Research** | `--mode=ai` | Ray + Dask + OpenAI MCP | Ray, Dask, OpenAI |
| 🧪 **Engineering / Simulation** | `--mode=engineering` | Simulink MCP + Python interface | Simulink, Python Interface |
| 💬 **AI-assisted Writing** | `--mode=writing` | LangChain + LangGraph MCP | LangChain, LangGraph |
| 🧭 **Experiment Management** | `--mode=experiment` | FastAPI + GitHub API + Shortcuts | FastAPI, GitHub, Shortcuts |
| 📚 **Cross-platform Notes / Literature** | `--mode=notes` | Obsidian MCP + Zotero API | Obsidian, Zotero |

## 📖 Usage Examples

### Basic Usage
```bash
# Start AI research mode
python mcp_hub.py --mode=ai

# Start note-taking mode  
python mcp_hub.py --mode=notes

# Start writing mode
python mcp_hub.py --mode=writing

# Show help
python mcp_hub.py --help
```

### Non-Interactive Mode
```bash
# Connect tools and exit (no interactive shell)
python mcp_hub.py --mode=ai --no-interactive
```

### Interactive Commands
Once the hub is running, you can use these commands:

```
MCP> help                    # Show available commands
MCP> status                  # Show hub and tool status  
MCP> tools                   # List all available tools
MCP> connect <tool>          # Connect to a specific tool
MCP> disconnect <tool>       # Disconnect from a specific tool
MCP> restart                 # Restart the hub
MCP> quit                    # Exit the hub
```

## 🏗️ Architecture

```
MCP_Terminal/
├── mcp_hub.py              # Main orchestration script
├── config.json             # Configuration file (auto-generated)
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── mcp_hub.log            # Log file (auto-generated)
└── tools/                 # MCP tool implementations
    ├── __init__.py
    ├── ray_mcp.py         # Ray distributed computing
    ├── openai_mcp.py      # OpenAI API integration
    ├── langchain_mcp.py   # LangChain framework
    ├── obsidian_mcp.py    # Obsidian note-taking
    └── ...                # Additional tools
```

## 🔧 Configuration

The hub automatically creates a `config.json` file with default settings:

```json
{
  "modes": {
    "ai": {
      "name": "Data Science / AI Research",
      "tools": ["ray", "dask", "openai"],
      "description": "Ray + Dask + OpenAI MCP for AI research"
    }
  },
  "settings": {
    "log_level": "INFO",
    "auto_reconnect": true,
    "max_retries": 3
  }
}
```

## 🛠️ Running in PyCharm

### Method 1: Terminal in PyCharm
1. Open PyCharm and navigate to the project folder
2. Open the terminal (View → Tool Windows → Terminal)
3. Run: `python mcp_hub.py --mode=ai`

### Method 2: Run Configuration
1. Right-click on `mcp_hub.py` in the project tree
2. Select "Run 'mcp_hub'"
3. Add command line arguments in Run Configuration:
   - Program arguments: `--mode=ai`
   - Working directory: `/path/to/MCP_Terminal`

### Method 3: Debug Mode
1. Set breakpoints in the code as needed
2. Right-click on `mcp_hub.py` → "Debug 'mcp_hub'"
3. Add arguments: `--mode=ai`

## 🔑 Environment Variables

Set these environment variables for full functionality:

```bash
# OpenAI API (for AI modes)
export OPENAI_API_KEY="your-openai-api-key"

# Obsidian Vault (for notes mode)
export OBSIDIAN_VAULT_PATH="/path/to/your/obsidian/vault"

# GitHub API (for experiment mode)
export GITHUB_TOKEN="your-github-token"
```

## 📝 Logging

The hub creates detailed logs in `mcp_hub.log`:

```
2024-01-17 10:30:15 - MCPHub - INFO - 🔌 Connecting to Ray cluster...
2024-01-17 10:30:15 - MCPHub - INFO - ✅ Ray MCP connected successfully
2024-01-17 10:30:16 - MCPHub - INFO - 🔌 Connecting to OpenAI API...
2024-01-17 10:30:16 - MCPHub - INFO - ✅ OpenAI MCP connected successfully
```

## 🚨 Troubleshooting

### Common Issues

1. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Permission Errors**
   ```bash
   chmod +x mcp_hub.py
   ```

3. **Python Version**
   ```bash
   python --version  # Should be 3.8+
   ```

4. **Port Conflicts**
   - Check if ports are already in use
   - Modify configuration if needed

### Getting Help

- Check the log file: `mcp_hub.log`
- Run with verbose logging: Modify log level in `config.json`
- Use `--help` flag: `python mcp_hub.py --help`

## 🔮 Future Extensions

The modular architecture makes it easy to add new MCP tools:

1. Create a new tool file in `tools/`
2. Implement the required methods
3. Add tool definition to `mcp_hub.py`
4. Update configuration

## 📄 License

This project is open source. Feel free to modify and distribute.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your MCP tool implementation
4. Test thoroughly
5. Submit a pull request

---

**Happy MCP Orchestrating! 🎉**
