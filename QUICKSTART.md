# 🚀 MCP Hub Quick Start Guide

## One-Command Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the hub
python mcp_hub.py --mode=ai
```

## Available Modes

| Command | What it does |
|---------|--------------|
| `python mcp_hub.py --mode=ai` | 🔬 Data Science / AI Research (Ray + Dask + OpenAI) |
| `python mcp_hub.py --mode=notes` | 📚 Cross-platform Notes (Obsidian + Zotero) |
| `python mcp_hub.py --mode=writing` | 💬 AI-assisted Writing (LangChain + LangGraph) |
| `python mcp_hub.py --mode=engineering` | 🧪 Engineering / Simulation (Simulink + Python) |
| `python mcp_hub.py --mode=experiment` | 🧭 Experiment Management (FastAPI + GitHub) |

## Interactive Commands

Once running, use these commands:
- `help` - Show all commands
- `status` - Show tool status
- `tools` - List available tools
- `quit` - Exit

## Environment Variables (Optional)

```bash
export OPENAI_API_KEY="your-key"           # For AI modes
export OBSIDIAN_VAULT_PATH="/path/to/vault" # For notes mode
export GITHUB_TOKEN="your-token"           # For experiment mode
```

## Troubleshooting

- **Missing dependencies**: Run `pip install -r requirements.txt`
- **Permission errors**: Run `chmod +x mcp_hub.py`
- **Check logs**: Look at `mcp_hub.log` file

## Demo

```bash
python demo.py  # See all modes in action
```

That's it! 🎉
