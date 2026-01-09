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
- **Untrusted code or sensitive systems**: Use container or local user (requires firewall configuration)
- **CI/CD environments**: Container isolation recommended
- **Maximum security**: Combine container with restricted network access

---

## DevContainers vs Native Sandbox

### Things DevContainers Can Do That Native Sandbox Cannot

| Capability | Why |
|------------|-----|
| Run a completely different OS/distro | Container can be Ubuntu while host is macOS |
| Isolate installed packages | `npm install -g` stays in container, doesn't pollute host |
| Run conflicting tool versions | Node 18 in one container, Node 22 in another |
| Provide service dependencies | Postgres, Redis, etc. via docker-compose |
| Guarantee reproducibility | Team shares identical environment via Dockerfile |
| Work on Windows | Native sandbox doesn't support Windows |
| Full environment reset | Delete container, rebuild fresh |
| Custom kernel parameters | sysctl settings, ulimits isolated to container |

### Things Native Sandbox Can Do That DevContainers Cannot

| Capability | Why |
|------------|-----|
| Access host GPU directly | No Docker GPU passthrough complexity |
| Use macOS-specific tools | Xcode, macOS Keychain, system frameworks |
| Native filesystem performance | No Docker volume overhead |
| Use host's authenticated tools | Your `gh`, `gcloud`, `aws` CLI sessions |
| Zero startup latency | No container boot time |
| Access host services | localhost services without port mapping |
| Lower memory footprint | No Docker daemon overhead |

---

## Network Isolation

Network isolation prevents Claude from exfiltrating data or downloading malicious payloads. While filesystem sandboxing limits local access, network restrictions prevent communication with unauthorized external services.

**Why it matters:**
- Prevents data exfiltration to arbitrary endpoints
- Blocks downloads of malicious scripts or binaries
- Limits exposure if Claude is compromised via prompt injection
- Provides audit trail of allowed network destinations

**Implementation approaches:**

| Method | Mechanism | Granularity |
|--------|-----------|-------------|
| Native sandbox | Host allowlist | Domain-level |
| Container firewall | iptables + ipset | IP/CIDR-level |
| Local user | iptables/pf rules | IP/port-level |
| Cloud-based | Cloud provider VPC/security groups | Full control |

**Our devcontainer approach** uses iptables with ipset to allow only specific IP ranges:
- Fetches GitHub IP ranges from `api.github.com/meta`
- Fetches AWS S3 IP ranges from `ip-ranges.amazonaws.com/ip-ranges.json`
- Resolves individual domains (PyPI, npm, Anthropic API) to IPs at startup
- Blocks all other outbound traffic

This is more robust than domain-based filtering because:
- DNS can be spoofed or tunneled
- CDNs share IPs across many domains
- IP allowlists are harder to bypass

See [DevContainer.md](DevContainer.md) for the full firewall configuration.

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
