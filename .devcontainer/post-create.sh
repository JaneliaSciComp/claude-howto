#!/bin/bash
set -e

# Initialize pixi environment and install package dependencies
pixi install

# Install Claude Code (host binary is macOS, need Linux version in container)
if ! command -v claude &> /dev/null; then
    echo "Installing Claude Code..."
    npm install -g @anthropic-ai/claude-code
fi

echo "Dev container setup complete!"
echo "Run 'claude --dangerously-skip-permissions' to start Claude Code"
echo "Run 'pixi run fileglancer' to start fileglancer"
