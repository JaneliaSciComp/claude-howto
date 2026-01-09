# Claude Code How-To

A collection of tips, tricks, and setup guides for running [Claude Code](https://docs.anthropic.com/en/docs/claude-code) at Janelia Research Campus.

## Getting Started

New to Claude Code? Start with the hands-on walkthrough that covers installation, permissions, planning mode, and practical exercises:

- [Getting Started Guide](docs/GettingStarted.md) - Janelia Claude-a-thon walkthrough with bug fixing, code analysis, and rapid prototyping exercises

## Sandboxing

Learn about the different sandboxing approaches and how to configure them:

- [Sandboxing Overview](docs/Sandboxing.md) - Comparison of native, container, and local user sandboxing methods
- [Native Sandbox](docs/NativeSandbox.md) - Using Claude Code's built-in OS-level sandbox
- [Dev Container Setup](docs/DevContainer.md) - Docker-based development environment with Python and Pixi

## Configuration

See [example-settings.json](example-settings.json) for an example Claude Code settings file that includes:
- Sandbox path permissions for Pixi
- Default permission mode configuration
- Allowed and denied operations

## Tools

This repository uses [Pixi](https://pixi.sh/) for Python environment management. Run `pixi install` to set up the environment.

### Dev Container

The included dev container runs Claude Code with network isolation (outbound traffic restricted to allowed domains). Requires Docker or Colima. See [Dev Container Setup](docs/DevContainer.md) for details.

These tasks are meant to be run OUTSIDE the container:

```bash
pixi run container-rebuild   # Build/rebuild the dev container
pixi run container-shell     # Open a shell in the container
pixi run container-claude    # Run Claude Code in the container
```

Once inside the container you can install dependencies and run Python commands:

```bash
pixi install
pixi run fileglancer start  # Run the Fileglancer bioimage browser
```
