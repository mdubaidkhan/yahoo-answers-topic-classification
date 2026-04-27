#!/bin/bash
# setup.sh
# Creates a virtual environment and installs all dependencies.

set -e

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo ""
echo "Setup complete. To activate the environment in the future, run:"
echo "  source .venv/bin/activate"
