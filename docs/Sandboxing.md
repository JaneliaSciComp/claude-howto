# Sandboxing Claude Code

Claude Code can execute arbitrary shell commands on your system. Sandboxing limits what those commands can access, protecting your system from unintended changes or data exposure.

There are three main approaches to sandboxing Claude Code:

## 1. Native Sandbox

Claude Code includes a built-in sandbox that uses OS-level mechanisms to restrict file and network access.

- **macOS**: Uses the Seatbelt framework (same technology as App Sandbox)
- **Linux**: Uses Landlock (kernel 5.13+) with seccomp fallback

**Pros:**
- Zero setup required - enabled by default
- Fine-grained control over file paths and network hosts
- Configurable via `/sandbox` command

**Cons:**
- Some tools may fail due to blocked system calls (see [NativeSandboxBug.md](NativeSandboxBug.md))
- macOS Seatbelt can block Mach IPC needed by some Rust crates

**Usage:**
```bash
# Sandbox is enabled by default
claude

# Check/modify sandbox settings
# Use /sandbox command within Claude Code
```

## 2. Container Isolation

Run Claude Code inside a Docker container, providing full OS-level isolation.

**Pros:**
- Complete isolation from host system
- Reproducible environment
- Works with VS Code Dev Containers

**Cons:**
- Requires Docker
- Some overhead for container management
- Need to mount Claude Code from host

**Usage:**

See [DevContainer.md](DevContainer.md) for a complete dev container setup.

Quick start:
```bash
npx @devcontainers/cli up --workspace-folder .
npx @devcontainers/cli exec --workspace-folder . bash -lc "claude --dangerously-skip-permissions"
```

## 3. Local User Account

Run Claude Code as a separate unprivileged user, using Unix permissions for isolation.

**Pros:**
- No container overhead
- Uses standard Unix security model
- Easy to understand and audit

**Cons:**
- Requires creating/managing a separate user
- Less granular than native sandbox
- Shared kernel with main user

**Usage:**

See [LocalUserAccount.md](LocalUserAccount.md) for setup instructions on macOS and Linux.

## Comparison

| Feature | Native Sandbox | Container | Local User |
|---------|---------------|-----------|------------|
| Setup complexity | None | Medium | Low |
| Isolation level | Process | OS | User |
| Performance overhead | Minimal | Low | None |
| File access control | Path-based | Mount-based | Permission-based |
| Network control | Host allowlist | Full | iptables/pf |
| GUI support | Yes | Limited | Yes (with config) |

## Recommendations

- **Development on trusted code**: Native sandbox (default) is usually sufficient
- **Untrusted code or sensitive systems**: Use container or local user isolation
- **CI/CD environments**: Container isolation recommended
- **Maximum security**: Combine container with restricted network access
