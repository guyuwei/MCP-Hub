#!/usr/bin/env python3
"""
MCP Hub Demo Script
==================

This script demonstrates the MCP Hub functionality with example usage.
"""

import asyncio
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path.cwd()))

from mcp_hub import MCPHub

async def demo_ai_mode():
    """Demonstrate AI research mode"""
    print("🔬 AI Research Mode Demo")
    print("=" * 40)
    
    hub = MCPHub(mode="ai")
    
    # Start hub
    success = await hub.start_hub()
    if not success:
        print("❌ Failed to start AI mode")
        return
    
    # Show status
    hub.show_status()
    
    # Simulate some work
    print("\n🧪 Simulating AI research workflow...")
    await asyncio.sleep(1)
    
    # Disconnect
    await hub.shutdown()
    print("✅ AI mode demo completed")

async def demo_notes_mode():
    """Demonstrate notes mode"""
    print("\n📚 Notes Mode Demo")
    print("=" * 40)
    
    hub = MCPHub(mode="notes")
    
    # Start hub
    success = await hub.start_hub()
    if not success:
        print("❌ Failed to start notes mode")
        return
    
    # Show status
    hub.show_status()
    
    # Simulate note-taking
    print("\n📝 Simulating note-taking workflow...")
    await asyncio.sleep(1)
    
    # Disconnect
    await hub.shutdown()
    print("✅ Notes mode demo completed")

async def demo_writing_mode():
    """Demonstrate writing mode"""
    print("\n💬 Writing Mode Demo")
    print("=" * 40)
    
    hub = MCPHub(mode="writing")
    
    # Start hub
    success = await hub.start_hub()
    if not success:
        print("❌ Failed to start writing mode")
        return
    
    # Show status
    hub.show_status()
    
    # Simulate writing workflow
    print("\n✍️  Simulating AI-assisted writing workflow...")
    await asyncio.sleep(1)
    
    # Disconnect
    await hub.shutdown()
    print("✅ Writing mode demo completed")

async def main():
    """Run all demos"""
    print("🎭 MCP Hub Demo")
    print("=" * 50)
    print("This demo showcases different MCP Hub modes")
    print("=" * 50)
    
    try:
        # Run demos
        await demo_ai_mode()
        await demo_notes_mode()
        await demo_writing_mode()
        
        print("\n🎉 All demos completed successfully!")
        print("\n💡 To run the full interactive hub:")
        print("   python mcp_hub.py --mode=ai")
        
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
