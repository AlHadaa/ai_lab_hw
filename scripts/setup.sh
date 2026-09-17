#!/usr/bin/env bash
# ==============================================================================
# Script: setup.sh
# Purpose: Automates Linux environment setup, virtual environment, & packages
# Course: AI Lab - Dr. Mohammed Al-Dhobaie
# ==============================================================================

set -e

echo "=================================================="
echo "🐧 [Linux Setup] Initializing SmartText AI Project"
echo "=================================================="

# 1. Check Python version
echo "[1/4] Checking Python installation..."
python3 --version || python --version

# 2. Create virtual environment if not present
if [ ! -d "venv" ]; then
    echo "[2/4] Creating virtual environment (.venv)..."
    python3 -m venv venv || python -m venv venv
else
    echo "[2/4] Virtual environment already exists."
fi

# 3. Activate virtual environment
echo "[3/4] Activating virtual environment..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
fi

# 4. Install dependencies
echo "[4/4] Installing required dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "=================================================="
echo "✅ Setup successfully completed!"
echo "Run the app using: ./scripts/run.sh"
echo "=================================================="
