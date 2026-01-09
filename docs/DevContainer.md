# Dev Container Usage

This dev container provides a complete development environment with Python and pixi, configured to run Claude Code.

## Prerequisites

- Container runtime (see platform-specific setup below)
- Node.js (for the devcontainer CLI)
- Claude Code configuration at `~/.claude` (Claude Code is installed inside the container)

### Linux

Install Docker using your distribution's package manager or [Docker's official instructions](https://docs.docker.com/engine/install/).

### macOS (Colima)

[Colima](https://github.com/abiosoft/colima) provides a lightweight alternative to Docker Desktop on macOS.

```bash
# Install Colima and Docker CLI
brew install colima docker

# Start Colima with recommended settings for devcontainers
colima start --cpu 4 --memory 8 --disk 60

# Verify Docker is working
docker ps
```

#### Manual vs Auto-Start

| Aspect | `colima start` | `brew services start colima` |
|--------|----------------|------------------------------|
| **Resource usage** | Only runs when you need it | Always running after login |
| **Control** | Easy to customize flags per session | Uses default or config file settings |
| **Battery/memory** | Saves resources when not developing | Constant background overhead |
| **Startup** | Manual, ~10-20 seconds | Automatic on login |

**Recommendation:** Use `colima start` directly unless you use containers daily. Start when needed, stop when done:

```bash
colima stop
```

If you prefer auto-start (for frequent container use):

```bash
brew services start colima
```

To save your preferred settings so you don't need flags each time, create `~/.colima/default/colima.yaml`:

```yaml
cpu: 4
memory: 8
disk: 60
```

## Host Mounts

The container mounts these directories from the host:
- `~/.claude` - Claude Code configuration (API keys, settings)

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
