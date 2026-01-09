# Sandboxing Claude Code

Claude Code can execute arbitrary shell commands on your system. Sandboxing limits what those commands can access, protecting your system from unintended changes or data exposure.

Why Sandboxing is Essential:
* **Security**: It prevents untrusted, dynamically generated code from harming your main system, protecting against prompt injection and malware.
* **Isolation**: Creates a virtual environment (like a mini-VM) with its own filesystem, runtime (Bash, Python), and network, isolating the agent from your actual development environment.
* **Autonomy**: Allows the agent to run commands and test code without constant user permission prompts, making workflows much faster (potentially even using flags like `--dangerously-skip-permissions`).
* **Resource Control**: Enforces boundaries on what the agent can access and do at the OS level

## Method Comparison

| Feature | Native Sandbox | Container | Local User | Cloud-based |
|---------|---------------|-----------|------------|-------------|
| Setup complexity | Low | Medium | Medium | Low |
| Isolation level | Process | OS | User | Full VM |
| Performance overhead | Minimal | Low | None | Variable |
| File access control | Path-based | Mount-based | Permission-based | Full isolation |
| Network control | Host allowlist | Full | iptables/pf | Full |
| Platform support | Linux, macOS | All (via Docker) | Linux, macOS | Any (browser) |

## Recommendations

- **Development on trusted code**: Native sandbox is usually sufficient (but has some issues on Mac)
- **Untrusted code or sensitive systems**: Use container or local user (requires configuration)
- **CI/CD environments**: Container isolation recommended
- **Maximum security**: Combine container with restricted network access

---

## Details

### Native Sandbox

Claude Code includes a built-in sandbox that uses OS-level mechanisms to restrict file and network access.

- **macOS**: Uses the Seatbelt framework (same technology as App Sandbox)
- **Linux**: Uses Landlock (kernel 5.13+) with seccomp fallback

**Pros:**
- Zero setup required - enabled by default
- Fine-grained control over file paths and network hosts
- Configurable via `/sandbox` command

**Cons:**
- Some tools may fail due to blocked system calls
- New feature, not well vetted
- Claude could escape if there are [bugs in Cladue Code](https://github.com/anthropics/claude-code/issues/15789)

See [NativeSandbox.md](NativeSandbox.md) for usage details and known issues.

### Container Isolation

Run Claude Code inside a Docker container, providing full OS-level isolation. Gold standard for agent isolation.

**Pros:**
- Complete isolation from host system
- Reproducible environment
- Works with VS Code Dev Containers

**Cons:**
- Some overhead for container management

See [DevContainer.md](DevContainer.md) for a complete dev container setup.

Quick start:
```bash
npx @devcontainers/cli up --workspace-folder .
npx @devcontainers/cli exec --workspace-folder . bash -lc "claude --dangerously-skip-permissions"
```

### Local User Account

> [!NOTE] 
> We haven't tried this yet. If you decide to try it out, please update this document with your findings.

Run Claude Code as a separate unprivileged user, using Unix permissions for isolation. This is missing network isolation and isn't recommended.

**Pros:**
- No container overhead
- Uses standard Unix security model
- Easy to understand and audit

**Cons:**
- Requires creating/managing a separate user
- No network isolation unless you configure it using a firewall
- Less granular than native sandbox
- Shared kernel with main user

### Cloud-based Environments

> [!NOTE] 
> We haven't tried this yet. If you decide to try it out, please update this document with your findings.

Run Claude Code in a cloud-hosted development environment, providing complete isolation from your local machine. 

**Options:**
- **AWS Cloud9**: IDE in the cloud with EC2 backend
- **Google Cloud Shell**: Browser-accessible shell with persistent storage
- **GitHub Codespaces**: Cloud-hosted dev containers with VS Code integration
- **Gitpod**: Browser-based workspaces with prebuilt environments

**Pros:**
- Complete isolation from local machine
- No local setup required beyond a browser
- Easily disposable - spin up fresh environments as needed
- Built-in compute resources (no local CPU/memory usage)
- Often includes free tiers for experimentation

**Cons:**
- May have latency compared to local development
- Cost for extended usage beyond free tiers
- Data lives on third-party infrastructure
- Some environments have session time limits
