#!/bin/bash
set -e

# Initialize network firewall (restricts outbound to allowed domains)
echo "Initializing network firewall..."
sudo /usr/local/bin/init-firewall.sh

# Fix ownership of .pixi volume (created as root by Docker)
sudo chown -R "$(id -u):$(id -g)" .pixi 2>/dev/null || true

# Initialize pixi environment and install package dependencies
pixi install

# Install Claude Code
if ! command -v claude &> /dev/null; then
    echo "Installing Claude Code..."
    npm install -g @anthropic-ai/claude-code
fi

echo "Dev container setup complete!"
echo "Run 'claude --dangerously-skip-permissions' to start Claude Code"
echo "Run 'pixi run example' to run the example script"
