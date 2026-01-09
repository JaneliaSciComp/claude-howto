# Claude Code How-To

A collection of tips, tricks, and setup guides for running [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Anthropic's official CLI for Claude.

## Getting Started

New to Claude Code? Start with the hands-on walkthrough that covers installation, permissions, planning mode, and practical exercises:

- [Getting Started Guide](docs/GettingStarted.md) - Janelia Claude-a-thon walkthrough with bug fixing, code analysis, and rapid prototyping exercises

## Sandboxing

Claude Code runs commands in a sandboxed environment by default. Learn about the different sandboxing approaches and how to configure them:

- [Sandboxing Overview](docs/Sandboxing.md) - Comparison of native, container, and local user sandboxing methods
- [Local User Account](docs/LocalUserAccount.md) - Create a dedicated unprivileged user for isolation on macOS/Linux
- [Native Sandbox Bug](docs/NativeSandboxBug.md) - Known issue with `pixi install` on macOS and workarounds

## Development Environment

Set up a reproducible development environment using Docker and dev containers:

- [Dev Container Setup](docs/DevContainer.md) - Docker-based development environment with Python and Pixi

## Configuration

See [example-settings.json](example-settings.json) for an example Claude Code settings file that includes:
- Sandbox path permissions for Pixi
- Default permission mode configuration
- Allowed and denied operations

## Tools

This repository uses [Pixi](https://pixi.sh/) for Python environment management. Run `pixi install` to set up the environment.

The project includes [Fileglancer](https://github.com/JaneliaSciComp/fileglancer), a file browser tool. Run it with:
```bash
pixi run fileglancer
```
