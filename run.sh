#!/bin/bash

# Set the path to the directory
USER_PATH=""

# Create the python environment
python3 -m venv "$USER_PATH"

# Activate the Python environment
source "$USER_PATH/bin/activate"

# Install the required packages
python3 -m pip install -r "$USER_PATH/requirements.txt"

# Run the Python script
python3 "$USER_PATH/script.py"