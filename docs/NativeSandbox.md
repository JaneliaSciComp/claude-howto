# Native Sandbox

Claude Code's native sandbox uses OS-level mechanisms to restrict what shell commands can access.

- **macOS**: Uses the Seatbelt framework (same technology as App Sandbox)
- **Linux**: Uses Landlock (kernel 5.13+) with seccomp fallback

## Usage

The sandbox is enabled by default. Use the `/sandbox` command within Claude Code to check or modify settings:

```
/sandbox          # View current sandbox status
/sandbox on       # Enable sandbox
/sandbox off      # Disable sandbox
```

## Configuration

Add allowed paths and hosts in your settings file:

```json
{
  "permissions": {
    "additionalSandboxPaths": [
      "/path/to/allow"
    ]
  }
}
```

## Known Issues

Some tools may fail due to blocked system calls. See [NativeSandboxBug.md](NativeSandboxBug.md) for a known issue with `pixi install` on macOS.
