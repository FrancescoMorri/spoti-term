#!/bin/bash

# Set the path to the directory
# USER_PATH=""
# Or use the current directory
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


# Activate the Python environment
source "$USER_PATH/bin/activate"

# Run the Python script
python3 "$USER_PATH/script.py"