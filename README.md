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

```bash
pixi run claude              # Run Claude Code in the dev container
pixi run container-rebuild   # Rebuild the dev container from scratch
pixi run fileglancer         # Run the Fileglancer bioimage browser
```
