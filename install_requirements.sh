#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Create the python environment
python3 -m venv "$SCRIPT_DIR"

# Activate the Python environment
source "$SCRIPT_DIR/bin/activate"

# Install the required packages
python3 -m pip install -r "$SCRIPT_DIR/requirements.txt"