#!/bin/bash
# MCP Hub Runner Script
# =====================
# Simple script to run the MCP Hub with different modes

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 MCP Hub Runner${NC}"
echo "================"

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo -e "${RED}❌ Python not found. Please install Python 3.8+${NC}"
    exit 1
fi

# Check if mcp_hub.py exists
if [ ! -f "mcp_hub.py" ]; then
    echo -e "${RED}❌ mcp_hub.py not found. Please run this script from the MCP_Terminal directory${NC}"
    exit 1
fi

# Function to show usage
show_usage() {
    echo -e "${YELLOW}Usage:${NC}"
    echo "  ./run_mcp.sh ai          # Data Science / AI Research"
    echo "  ./run_mcp.sh notes       # Cross-platform Notes"
    echo "  ./run_mcp.sh writing     # AI-assisted Writing"
    echo "  ./run_mcp.sh engineering # Engineering / Simulation"
    echo "  ./run_mcp.sh experiment  # Experiment Management"
    echo "  ./run_mcp.sh demo        # Run demo"
    echo "  ./run_mcp.sh setup       # Setup dependencies"
    echo "  ./run_mcp.sh help        # Show this help"
}

# Function to run setup
run_setup() {
    echo -e "${YELLOW}🔧 Setting up MCP Hub...${NC}"
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        echo -e "${GREEN}✅ Setup completed${NC}"
    else
        echo -e "${RED}❌ requirements.txt not found${NC}"
        exit 1
    fi
}

# Function to run demo
run_demo() {
    echo -e "${YELLOW}🎭 Running MCP Hub Demo...${NC}"
    python demo.py
}

# Main logic
case "$1" in
    "ai")
        echo -e "${GREEN}🔬 Starting AI Research Mode...${NC}"
        python mcp_hub.py --mode=ai
        ;;
    "notes")
        echo -e "${GREEN}📚 Starting Notes Mode...${NC}"
        python mcp_hub.py --mode=notes
        ;;
    "writing")
        echo -e "${GREEN}💬 Starting Writing Mode...${NC}"
        python mcp_hub.py --mode=writing
        ;;
    "engineering")
        echo -e "${GREEN}🧪 Starting Engineering Mode...${NC}"
        python mcp_hub.py --mode=engineering
        ;;
    "experiment")
        echo -e "${GREEN}🧭 Starting Experiment Mode...${NC}"
        python mcp_hub.py --mode=experiment
        ;;
    "demo")
        run_demo
        ;;
    "setup")
        run_setup
        ;;
    "help"|"-h"|"--help"|"")
        show_usage
        ;;
    *)
        echo -e "${RED}❌ Unknown mode: $1${NC}"
        show_usage
        exit 1
        ;;
esac
