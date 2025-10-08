#!/usr/bin/env python3
"""
Setup script for MCP Hub
========================

This script helps set up the MCP Hub environment and install dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required, found {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    # Check if requirements.txt exists
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found")
        return False
    
    # Install dependencies
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing Python packages"
    )

def create_config():
    """Create default configuration"""
    print("⚙️  Setting up configuration...")
    
    config_path = Path("config.json")
    if config_path.exists():
        print("✅ Configuration file already exists")
        return True
    
    # The config will be created automatically by mcp_hub.py
    print("✅ Configuration will be created on first run")
    return True

def test_installation():
    """Test the installation"""
    print("🧪 Testing installation...")
    
    # Test import of main modules
    try:
        import asyncio
        import argparse
        import logging
        import json
        from pathlib import Path
        from typing import Dict, List, Optional, Any
        from dataclasses import dataclass
        from datetime import datetime
        print("✅ Core Python modules imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import core modules: {e}")
        return False
    
    # Test if mcp_hub.py can be imported
    try:
        # Add current directory to path
        sys.path.insert(0, str(Path.cwd()))
        import mcp_hub
        print("✅ MCP Hub module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import MCP Hub: {e}")
        return False
    
    return True

def main():
    """Main setup function"""
    print("🚀 MCP Hub Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed during dependency installation")
        sys.exit(1)
    
    # Create configuration
    if not create_config():
        print("❌ Setup failed during configuration")
        sys.exit(1)
    
    # Test installation
    if not test_installation():
        print("❌ Setup failed during testing")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📖 Next steps:")
    print("1. Set environment variables (optional):")
    print("   export OPENAI_API_KEY='your-key'")
    print("   export OBSIDIAN_VAULT_PATH='/path/to/vault'")
    print("\n2. Run the MCP Hub:")
    print("   python mcp_hub.py --mode=ai")
    print("\n3. For help:")
    print("   python mcp_hub.py --help")

if __name__ == "__main__":
    main()
