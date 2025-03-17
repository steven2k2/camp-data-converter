#!/bin/bash

# Define project root
PROJECT_DIR=$(pwd)

echo "🚀 Setting up Camp Data Converter..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install it and try again."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Final setup message
echo "Setup complete! To activate the virtual environment, run:"
echo "source venv/bin/activate  # macOS/Linux"
echo "venv\\Scripts\\activate   # Windows"

# Ensure execute permissions for scripts
chmod +x scripts/*.sh

echo "You can now run the conversion scripts!"
