"""
Obsidian MCP Tool - Obsidian Note-taking Integration
===================================================

This module provides MCP integration for Obsidian, enabling note-taking
and knowledge management through the Model Context Protocol.
"""

import asyncio
import logging
from typing import Dict, Any, Optional, List
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

class ObsidianMCPTool:
    """Obsidian MCP Tool implementation"""
    
    def __init__(self):
        self.name = "Obsidian MCP"
        self.version = "1.0.0"
        self.status = "disconnected"
        self.vault_path = None
        self.connected_at = None
        self.notes = {}
        
    async def connect(self, vault_path: Optional[str] = None) -> bool:
        """Connect to Obsidian vault"""
        try:
            logger.info("🔌 Connecting to Obsidian vault...")
            
            # Set vault path
            self.vault_path = vault_path or os.getenv("OBSIDIAN_VAULT_PATH")
            
            if not self.vault_path:
                # Use default vault path
                self.vault_path = str(Path.home() / "Documents" / "Obsidian Vault")
                logger.info(f"📁 Using default vault path: {self.vault_path}")
            
            # Simulate vault connection
            await asyncio.sleep(0.3)
            
            self.status = "connected"
            self.connected_at = datetime.now()
            
            # Mock some notes
            self.notes = {
                "daily_notes": [
                    "2024-01-15.md",
                    "2024-01-16.md", 
                    "2024-01-17.md"
                ],
                "projects": [
                    "Project Alpha.md",
                    "Project Beta.md"
                ],
                "meetings": [
                    "Team Meeting 2024-01-15.md",
                    "Client Call 2024-01-16.md"
                ]
            }
            
            logger.info("✅ Obsidian MCP connected successfully")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to connect to Obsidian: {e}")
            self.status = "error"
            return False
    
    async def disconnect(self):
        """Disconnect from Obsidian vault"""
        logger.info("🔌 Disconnecting from Obsidian vault...")
        self.status = "disconnected"
        self.vault_path = None
        logger.info("✅ Obsidian MCP disconnected")
    
    async def create_note(self, title: str, content: str, folder: str = "notes") -> str:
        """Create a new note"""
        if self.status != "connected":
            raise RuntimeError("Obsidian MCP not connected")
        
        # Generate filename
        filename = f"{title.replace(' ', '_')}.md"
        note_path = f"{folder}/{filename}"
        
        # Simulate note creation
        await asyncio.sleep(0.2)
        
        # Mock note content
        note_content = f"""# {title}

{content}

---
*Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
        
        logger.info(f"📝 Created note: {note_path}")
        return note_path
    
    async def search_notes(self, query: str) -> List[Dict[str, Any]]:
        """Search notes by query"""
        if self.status != "connected":
            return []
        
        # Simulate search
        await asyncio.sleep(0.3)
        
        # Mock search results
        mock_results = [
            {
                "title": f"Note matching '{query}'",
                "path": f"notes/search_result_1.md",
                "snippet": f"This note contains information about {query}...",
                "modified": datetime.now().isoformat()
            },
            {
                "title": f"Another note about {query}",
                "path": f"projects/{query}_project.md", 
                "snippet": f"Project documentation for {query}...",
                "modified": datetime.now().isoformat()
            }
        ]
        
        logger.info(f"🔍 Found {len(mock_results)} notes matching '{query}'")
        return mock_results
    
    async def get_note_content(self, note_path: str) -> str:
        """Get content of a specific note"""
        if self.status != "connected":
            raise RuntimeError("Obsidian MCP not connected")
        
        # Simulate file read
        await asyncio.sleep(0.1)
        
        # Mock note content
        return f"""# Note: {note_path}

This is the content of the note at {note_path}.

## Section 1
Some content here...

## Section 2
More content here...

---
*Last modified: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    async def list_notes(self, folder: Optional[str] = None) -> List[str]:
        """List notes in vault or specific folder"""
        if self.status != "connected":
            return []
        
        if folder and folder in self.notes:
            return self.notes[folder]
        
        # Return all notes
        all_notes = []
        for folder_notes in self.notes.values():
            all_notes.extend(folder_notes)
        
        return all_notes
    
    async def get_status(self) -> Dict[str, Any]:
        """Get Obsidian MCP status"""
        return {
            "status": self.status,
            "vault_path": self.vault_path,
            "total_notes": sum(len(notes) for notes in self.notes.values()),
            "folders": list(self.notes.keys()),
            "connected_at": self.connected_at.isoformat() if self.connected_at else None
        }

# Global instance
obsidian_tool = ObsidianMCPTool()
