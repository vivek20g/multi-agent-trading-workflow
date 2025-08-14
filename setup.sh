#!/bin/bash

# Install system dependencies via Homebrew
echo "Installing system dependencies with Homebrew..."
brew update
brew install ta-lib


# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate


# Upgrade pip and install Python dependencies
echo "Installing Python dependencies with pip..."
pip install --upgrade pip
pip install -r requirements_macOS.txt

echo "Setup complete."
