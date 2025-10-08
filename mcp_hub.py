#!/usr/bin/env python3
"""
MCP Hub - Standalone Model Context Protocol Orchestration Script
================================================================

A local MCP hub that connects and coordinates multiple Model Context Protocol tools.
Works without Cursor - only requires Python and a terminal.

Usage:
    python mcp_hub.py --mode=ai          # Data Science / AI Research
    python mcp_hub.py --mode=engineering # Engineering / Simulation  
    python mcp_hub.py --mode=writing     # AI-assisted Writing
    python mcp_hub.py --mode=experiment  # Experiment Management
    python mcp_hub.py --mode=notes       # Cross-platform Notes / Literature
    python mcp_hub.py --help             # Show help
"""

import asyncio
import argparse
import logging
import sys
import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('mcp_hub.log')
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class MCPTool:
    """Represents an MCP tool configuration"""
    name: str
    description: str
    module: str
    dependencies: List[str]
    status: str = "disconnected"
    last_activity: Optional[datetime] = None

class MCPHub:
    """Main MCP Hub orchestrator"""
    
    def __init__(self, mode: str = "ai"):
        self.mode = mode
        self.tools: Dict[str, MCPTool] = {}
        self.active_connections: Dict[str, Any] = {}
        self.config = self._load_config()
        self.setup_tools()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from config.json or create default"""
        config_path = Path("config.json")
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not load config.json: {e}")
        
        # Default configuration
        default_config = {
            "modes": {
                "ai": {
                    "name": "Data Science / AI Research",
                    "tools": ["ray", "dask", "openai"],
                    "description": "Ray + Dask + OpenAI MCP for AI research"
                },
                "engineering": {
                    "name": "Engineering / Simulation", 
                    "tools": ["simulink", "python_interface"],
                    "description": "Simulink MCP + Python interface"
                },
                "writing": {
                    "name": "AI-assisted Writing",
                    "tools": ["langchain", "langgraph"],
                    "description": "LangChain + LangGraph MCP"
                },
                "experiment": {
                    "name": "Experiment Management",
                    "tools": ["fastapi", "github", "shortcuts"],
                    "description": "FastAPI + GitHub API + Shortcuts"
                },
                "notes": {
                    "name": "Cross-platform Notes / Literature",
                    "tools": ["obsidian", "zotero"],
                    "description": "Obsidian MCP + Zotero API"
                }
            },
            "settings": {
                "log_level": "INFO",
                "auto_reconnect": True,
                "max_retries": 3
            }
        }
        
        # Save default config
        with open(config_path, 'w') as f:
            json.dump(default_config, f, indent=2)
        
        return default_config
    
    def setup_tools(self):
        """Initialize tool configurations based on mode"""
        if self.mode not in self.config["modes"]:
            raise ValueError(f"Unknown mode: {self.mode}. Available modes: {list(self.config['modes'].keys())}")
        
        mode_config = self.config["modes"][self.mode]
        tool_names = mode_config["tools"]
        
        # Tool definitions
        tool_definitions = {
            "ray": MCPTool(
                name="Ray",
                description="Distributed computing framework for ML/AI workloads",
                module="tools.ray_mcp",
                dependencies=["ray", "fastmcp"]
            ),
            "dask": MCPTool(
                name="Dask", 
                description="Parallel computing library for analytics",
                module="tools.dask_mcp",
                dependencies=["dask", "fastmcp"]
            ),
            "openai": MCPTool(
                name="OpenAI MCP",
                description="OpenAI API integration for AI models",
                module="tools.openai_mcp", 
                dependencies=["openai", "fastmcp"]
            ),
            "simulink": MCPTool(
                name="Simulink MCP",
                description="MATLAB Simulink integration",
                module="tools.simulink_mcp",
                dependencies=["matlab", "fastmcp"]
            ),
            "python_interface": MCPTool(
                name="Python Interface",
                description="Python scripting interface",
                module="tools.python_interface",
                dependencies=["fastmcp"]
            ),
            "langchain": MCPTool(
                name="LangChain MCP",
                description="LangChain framework integration",
                module="tools.langchain_mcp",
                dependencies=["langchain", "fastmcp"]
            ),
            "langgraph": MCPTool(
                name="LangGraph MCP", 
                description="LangGraph workflow integration",
                module="tools.langgraph_mcp",
                dependencies=["langgraph", "fastmcp"]
            ),
            "fastapi": MCPTool(
                name="FastAPI MCP",
                description="FastAPI web framework integration",
                module="tools.fastapi_mcp",
                dependencies=["fastapi", "uvicorn", "fastmcp"]
            ),
            "github": MCPTool(
                name="GitHub API MCP",
                description="GitHub API integration",
                module="tools.github_mcp",
                dependencies=["requests", "fastmcp"]
            ),
            "shortcuts": MCPTool(
                name="Shortcuts MCP",
                description="System shortcuts integration",
                module="tools.shortcuts_mcp",
                dependencies=["fastmcp"]
            ),
            "obsidian": MCPTool(
                name="Obsidian MCP",
                description="Obsidian note-taking integration",
                module="tools.obsidian_mcp",
                dependencies=["requests", "fastmcp"]
            ),
            "zotero": MCPTool(
                name="Zotero API MCP",
                description="Zotero reference management integration",
                module="tools.zotero_mcp",
                dependencies=["requests", "fastmcp"]
            )
        }
        
        # Add tools for current mode
        for tool_name in tool_names:
            if tool_name in tool_definitions:
                self.tools[tool_name] = tool_definitions[tool_name]
            else:
                logger.warning(f"Unknown tool: {tool_name}")
    
    async def check_dependencies(self) -> bool:
        """Check if all required dependencies are installed"""
        logger.info("🔍 Checking dependencies...")
        missing_deps = []
        
        for tool_name, tool in self.tools.items():
            for dep in tool.dependencies:
                try:
                    __import__(dep)
                    logger.info(f"✅ {dep} - OK")
                except ImportError:
                    missing_deps.append(dep)
                    logger.error(f"❌ {dep} - Missing")
        
        if missing_deps:
            logger.error(f"Missing dependencies: {', '.join(missing_deps)}")
            logger.info("Install with: pip install " + " ".join(missing_deps))
            return False
        
        logger.info("✅ All dependencies satisfied")
        return True
    
    async def connect_tool(self, tool_name: str) -> bool:
        """Connect to a specific MCP tool"""
        tool = self.tools.get(tool_name)
        if not tool:
            logger.error(f"Tool {tool_name} not found")
            return False
        
        try:
            logger.info(f"🔌 Connecting to {tool.name}...")
            
            # Simulate tool connection (replace with actual MCP connection logic)
            await asyncio.sleep(0.5)  # Simulate connection time
            
            tool.status = "connected"
            tool.last_activity = datetime.now()
            self.active_connections[tool_name] = {
                "tool": tool,
                "connected_at": datetime.now(),
                "status": "active"
            }
            
            logger.info(f"✅ {tool.name} connected successfully")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to connect to {tool.name}: {e}")
            tool.status = "error"
            return False
    
    async def disconnect_tool(self, tool_name: str):
        """Disconnect from a specific MCP tool"""
        if tool_name in self.active_connections:
            tool = self.tools[tool_name]
            logger.info(f"🔌 Disconnecting from {tool.name}...")
            
            # Simulate disconnection
            await asyncio.sleep(0.2)
            
            tool.status = "disconnected"
            del self.active_connections[tool_name]
            logger.info(f"✅ {tool.name} disconnected")
    
    async def start_hub(self):
        """Start the MCP hub and connect all tools"""
        mode_config = self.config["modes"][self.mode]
        
        print(f"\n🚀 Starting MCP Hub - {mode_config['name']}")
        print(f"📋 Mode: {self.mode}")
        print(f"📝 Description: {mode_config['description']}")
        print(f"🔧 Tools: {', '.join(self.tools.keys())}")
        print("=" * 60)
        
        # Check dependencies
        if not await self.check_dependencies():
            logger.error("❌ Dependency check failed. Please install missing packages.")
            return False
        
        # Connect to all tools
        logger.info("🔌 Connecting to MCP tools...")
        connection_tasks = []
        
        for tool_name in self.tools.keys():
            task = asyncio.create_task(self.connect_tool(tool_name))
            connection_tasks.append(task)
        
        # Wait for all connections
        results = await asyncio.gather(*connection_tasks, return_exceptions=True)
        
        # Check results
        successful_connections = sum(1 for result in results if result is True)
        total_tools = len(self.tools)
        
        if successful_connections == total_tools:
            logger.info(f"✅ All {total_tools} tools connected successfully!")
        else:
            logger.warning(f"⚠️  {successful_connections}/{total_tools} tools connected")
        
        return successful_connections > 0
    
    async def run_interactive_mode(self):
        """Run interactive mode for user commands"""
        print(f"\n🎯 MCP Hub is ready! Type 'help' for commands or 'quit' to exit.")
        print("=" * 60)
        
        # 显示API使用示例
        self.show_api_examples()
        
        while True:
            try:
                command = input("\nMCP> ").strip().lower()
                
                if command in ['quit', 'exit', 'q']:
                    break
                elif command == 'help':
                    self.show_help()
                elif command == 'status':
                    self.show_status()
                elif command == 'tools':
                    self.list_tools()
                elif command == 'api':
                    self.show_api_examples()
                elif command.startswith('connect '):
                    tool_name = command.split(' ', 1)[1]
                    await self.connect_tool(tool_name)
                elif command.startswith('disconnect '):
                    tool_name = command.split(' ', 1)[1]
                    await self.disconnect_tool(tool_name)
                elif command == 'restart':
                    await self.restart_hub()
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                logger.error(f"Error in interactive mode: {e}")
    
    def show_api_examples(self):
        """Show API usage examples for connected tools"""
        print("\n🚀 API使用示例:")
        print("=" * 50)
        
        for tool_name, tool in self.tools.items():
            if tool.status == "connected":
                print(f"\n🔧 {tool.name} API:")
                
                if tool_name == "ray":
                    print("  # 分布式计算示例")
                    print("  import ray")
                    print("  ray.init()")
                    print("  ")
                    print("  @ray.remote")
                    print("  def process_data(data):")
                    print("      return data * 2")
                    print("  ")
                    print("  futures = [process_data.remote(i) for i in range(10)]")
                    print("  results = ray.get(futures)")
                    print("  ray.shutdown()")
                
                elif tool_name == "dask":
                    print("  # 大数据处理示例")
                    print("  import dask.array as da")
                    print("  ")
                    print("  x = da.random.random((1000, 1000), chunks=(100, 100))")
                    print("  result = (x + x.T).sum()")
                    print("  result.compute()")
                
                elif tool_name == "openai":
                    print("  # OpenAI API示例")
                    print("  import openai")
                    print("  ")
                    print("  response = openai.ChatCompletion.create(")
                    print("      model='gpt-3.5-turbo',")
                    print("      messages=[{'role': 'user', 'content': 'Hello!'}]")
                    print("  )")
                    print("  print(response.choices[0].message.content)")
                
                elif tool_name == "langchain":
                    print("  # LangChain API示例")
                    print("  from langchain.llms import OpenAI")
                    print("  from langchain.chains import LLMChain")
                    print("  ")
                    print("  llm = OpenAI(temperature=0.7)")
                    print("  chain = LLMChain(llm=llm, prompt=prompt)")
                    print("  result = chain.run('Hello World')")
                
                elif tool_name == "langgraph":
                    print("  # LangGraph API示例")
                    print("  from langgraph import StateGraph, END")
                    print("  ")
                    print("  workflow = StateGraph(WorkflowState)")
                    print("  workflow.add_node('process', process_node)")
                    print("  workflow.add_edge('process', END)")
                    print("  app = workflow.compile()")
                
                elif tool_name == "fastapi":
                    print("  # FastAPI示例")
                    print("  from fastapi import FastAPI")
                    print("  ")
                    print("  app = FastAPI()")
                    print("  ")
                    print("  @app.get('/')")
                    print("  async def root():")
                    print("      return {'message': 'Hello World'}")
                
                elif tool_name == "obsidian":
                    print("  # Obsidian笔记管理示例")
                    print("  import os")
                    print("  ")
                    print("  def read_note(file_path):")
                    print("      with open(file_path, 'r', encoding='utf-8') as f:")
                    print("          return f.read()")
                    print("  ")
                    print("  def create_note(file_path, content):")
                    print("      with open(file_path, 'w', encoding='utf-8') as f:")
                    print("          f.write(content)")
                
                print()
        
        print("💡 提示: 输入 'help' 查看更多命令，输入 'quit' 退出")

    def show_help(self):
        """Show available commands"""
        print("\n📖 Available Commands:")
        print("  help                    - Show this help message")
        print("  status                  - Show hub and tool status")
        print("  tools                   - List all available tools")
        print("  api                     - Show API usage examples")
        print("  connect <tool>          - Connect to a specific tool")
        print("  disconnect <tool>       - Disconnect from a specific tool")
        print("  restart                 - Restart the hub")
        print("  quit/exit/q             - Exit the hub")
    
    def show_status(self):
        """Show current hub status"""
        print(f"\n📊 MCP Hub Status:")
        print(f"  Mode: {self.mode}")
        print(f"  Active Connections: {len(self.active_connections)}")
        print(f"  Total Tools: {len(self.tools)}")
        
        print(f"\n🔧 Tool Status:")
        for tool_name, tool in self.tools.items():
            status_icon = "✅" if tool.status == "connected" else "❌" if tool.status == "error" else "⚪"
            print(f"  {status_icon} {tool.name}: {tool.status}")
    
    def list_tools(self):
        """List all available tools"""
        print(f"\n🔧 Available Tools:")
        for tool_name, tool in self.tools.items():
            print(f"  • {tool.name} ({tool_name})")
            print(f"    Description: {tool.description}")
            print(f"    Status: {tool.status}")
            print()
    
    async def restart_hub(self):
        """Restart the hub"""
        logger.info("🔄 Restarting MCP Hub...")
        
        # Disconnect all tools
        for tool_name in list(self.active_connections.keys()):
            await self.disconnect_tool(tool_name)
        
        # Reconnect
        await self.start_hub()
    
    async def shutdown(self):
        """Gracefully shutdown the hub"""
        logger.info("🛑 Shutting down MCP Hub...")
        
        # Disconnect all tools
        for tool_name in list(self.active_connections.keys()):
            await self.disconnect_tool(tool_name)
        
        logger.info("✅ MCP Hub shutdown complete")

async def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="MCP Hub - Standalone Model Context Protocol Orchestration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python mcp_hub.py --mode=ai          # Data Science / AI Research
  python mcp_hub.py --mode=notes       # Cross-platform Notes / Literature
  python mcp_hub.py --mode=writing     # AI-assisted Writing
  python mcp_hub.py --help             # Show this help
        """
    )
    
    parser.add_argument(
        '--mode', 
        choices=['ai', 'engineering', 'writing', 'experiment', 'notes'],
        default='ai',
        help='MCP tool combination mode (default: ai)'
    )
    
    parser.add_argument(
        '--no-interactive',
        action='store_true',
        help='Run without interactive mode (just connect and exit)'
    )
    
    args = parser.parse_args()
    
    try:
        # Create and start hub
        hub = MCPHub(mode=args.mode)
        
        # Start the hub
        success = await hub.start_hub()
        
        if success and not args.no_interactive:
            # Run interactive mode
            await hub.run_interactive_mode()
        elif success:
            print("✅ MCP Hub started successfully (non-interactive mode)")
        else:
            print("❌ MCP Hub failed to start")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n👋 Interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        if 'hub' in locals():
            await hub.shutdown()

if __name__ == "__main__":
    # Create tools directory if it doesn't exist
    tools_dir = Path("tools")
    tools_dir.mkdir(exist_ok=True)
    
    # Create __init__.py in tools directory
    init_file = tools_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text("# MCP Tools Package\n")
    
    # Run the main function
    asyncio.run(main())
