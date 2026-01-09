# Claude Code How-To Repository

Documentation and configuration for running Claude Code safely at Janelia Research Campus.

## Project Structure

```
├── .devcontainer/          # Dev container configuration
│   ├── Dockerfile          # Container image with pixi and firewall tools
│   ├── devcontainer.json   # VS Code/CLI devcontainer config
│   ├── init-firewall.sh    # iptables firewall restricting outbound network
│   └── post-create.sh      # Runs on container start (firewall + pixi install)
├── docs/                   # Documentation
│   ├── DevContainer.md     # Container setup and usage
│   ├── GettingStarted.md   # Claude-a-thon walkthrough
│   ├── LocalUserAccount.md # Unprivileged user sandboxing
│   ├── NativeSandbox.md    # Built-in sandbox usage
│   ├── NativeSandboxBug.md # macOS pixi issue
│   └── Sandboxing.md       # Overview of sandboxing approaches
├── example.py              # Example Python script (fetches zarr metadata from S3)
├── example-settings.json   # Example Claude Code settings
├── pixi.toml               # Pixi package manager config
└── README.md               # Project overview
```

## Key Commands

```bash
pixi install                 # Set up local environment
pixi run container-rebuild   # Build/rebuild the dev container
pixi run container-shell     # Open a shell in the container
pixi run claude              # Run Claude Code in the container
pixi run example             # Run the example Python script
```

## Dev Container

The dev container provides network-isolated Claude Code execution:

- **Firewall**: iptables restricts outbound traffic to allowed domains only
- **Privacy**: Telemetry disabled via environment variables
- **Mounts**: `~/.claude` from host for API keys/auth

To add allowed domains, edit `.devcontainer/init-firewall.sh` and add to the `ALLOWED_DOMAINS` array.

To disable firewall at runtime: `sudo iptables -F && sudo iptables -P INPUT ACCEPT && sudo iptables -P OUTPUT ACCEPT`

## Documentation Guidelines

- Keep docs concise and practical
- Put comparison tables and recommendations at the top
- Details and step-by-step instructions below
- Link between related docs rather than duplicating content

## Dependencies

- Pixi for Python environment management
- Docker/Colima for container runtime
- Node.js for devcontainer CLI and Claude Code
