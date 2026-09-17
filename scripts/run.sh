#!/usr/bin/env bash
# ==============================================================================
# Script: run.sh
# Purpose: Starts the Flask Web Server in Linux environment
# Course: AI Lab - Dr. Mohammed Al-Dhobaie
# ==============================================================================

set -e

echo "🚀 Launching SmartText AI & Vibe Studio..."

# Activate virtual environment if available
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
fi

# Export environment variables
export FLASK_APP=run.py
export FLASK_DEBUG=True
export PORT=5000

echo "🌐 Access application at: http://127.0.0.1:5000"
python run.py
