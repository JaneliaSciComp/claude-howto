# Dev Container Usage

This dev container provides a complete development environment with Python and pixi, configured to run Claude Code.

## Prerequisites

- Docker installed and running
- Node.js (for the devcontainer CLI)
- Claude Code installed on the host at `~/.local/bin/claude`

## Host Mounts

The container mounts these directories from the host:
- `~/.claude` - Claude Code configuration
- `~/.local/bin` - Local binaries including Claude (readonly)
- `~/.local/share/claude` - Claude Code installation

## Quick Start

```bash
# Build and start the container
npx @devcontainers/cli up --workspace-folder .

# Get a shell inside the container
npx @devcontainers/cli exec --workspace-folder . bash
```

## Commands

### Start the Container

```bash
npx @devcontainers/cli up --workspace-folder .
```

### Open a Shell

```bash
npx @devcontainers/cli exec --workspace-folder . bash
```

### Run Claude Code

```bash
# From inside the container shell
claude --dangerously-skip-permissions

# Or directly (use bash -lc to get proper PATH)
npx @devcontainers/cli exec --workspace-folder . bash -lc "claude --dangerously-skip-permissions"
```

### Run Fileglancer

```bash
# Inside the container
pixi run fileglancer
```

### Stop the Container

```bash
# Find the container ID
docker ps | grep claude-howto

# Stop it
docker stop <container_id>
```

### Rebuild from Scratch

Use this after modifying Dockerfile or devcontainer.json:

```bash
npx @devcontainers/cli up --workspace-folder . --remove-existing-container
```

## Inside the Container

| Command | Description |
|---------|-------------|
| `pixi install` | Install pixi dependencies |
| `pixi run fileglancer` | Run the fileglancer CLI |
| `claude` | Claude Code CLI |

## VS Code / Cursor

You can also open the project in VS Code or Cursor and use the "Reopen in Container" command for a GUI-based experience.
