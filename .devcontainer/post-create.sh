#!/bin/bash
set -e

# Initialize pixi environment and install package dependencies
pixi install

echo "Dev container setup complete!"
echo "Run 'pixi run fileglancer' to start fileglancer"
