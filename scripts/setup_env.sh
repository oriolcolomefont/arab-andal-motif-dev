#!/bin/bash
set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Setting up virtual environment for Arab-Andalusian motif analysis...${NC}"

# Create virtual environment
echo -e "\n${GREEN}Creating virtual environment...${NC}"
python3 -m venv .venv

# Activate virtual environment
echo -e "\n${GREEN}Activating virtual environment...${NC}"
source .venv/bin/activate

# Upgrade pip
echo -e "\n${GREEN}Upgrading pip...${NC}"
pip install --upgrade pip

# Install requirements
echo -e "\n${GREEN}Installing requirements...${NC}"
pip install -r requirements.txt

# Install pre-commit hooks
echo -e "\n${GREEN}Installing pre-commit hooks...${NC}"
pre-commit install

# Run environment validation
echo -e "\n${GREEN}Validating environment...${NC}"
python scripts/validate_env.py

echo -e "\n${GREEN}Setup complete!${NC}"
echo -e "${YELLOW}To activate the virtual environment, run:${NC}"
echo -e "source .venv/bin/activate" 