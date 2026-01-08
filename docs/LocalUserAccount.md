# Local User Account Sandboxing

Run Claude Code as a separate unprivileged user to isolate it from your main account using standard Unix permissions.

## Overview

This approach creates a dedicated user account for running Claude Code. The user can only access:
- Its own home directory
- Specific project directories you explicitly share
- System files readable by all users

## macOS Setup

### Create the User

```bash
# Create a new user (requires admin password)
sudo dscl . -create /Users/claude-sandbox
sudo dscl . -create /Users/claude-sandbox UserShell /bin/zsh
sudo dscl . -create /Users/claude-sandbox RealName "Claude Sandbox"
sudo dscl . -create /Users/claude-sandbox UniqueID 550
sudo dscl . -create /Users/claude-sandbox PrimaryGroupID 20
sudo dscl . -create /Users/claude-sandbox NFSHomeDirectory /Users/claude-sandbox

# Create and set ownership of home directory
sudo mkdir -p /Users/claude-sandbox
sudo chown -R claude-sandbox:staff /Users/claude-sandbox

# Set a password (you'll be prompted)
sudo dscl . -passwd /Users/claude-sandbox
```

### Install Claude Code for the Sandbox User

```bash
# Switch to the sandbox user
su - claude-sandbox

# Install Claude Code
curl -fsSL https://claude.ai/install.sh | sh

# Authenticate with Anthropic
claude auth login
```

### Share a Project Directory

```bash
# From your main account, give the sandbox user access to a project
# Option 1: Change group ownership (both users in 'staff' group)
chmod -R g+rwX /path/to/project

# Option 2: Use ACLs for more control
chmod +a "claude-sandbox allow read,write,execute,delete,add_file,add_subdirectory" /path/to/project
```

### Run Claude Code

```bash
# Switch to sandbox user and run claude
su - claude-sandbox -c "cd /path/to/project && claude"

# Or use sudo
sudo -u claude-sandbox -i sh -c "cd /path/to/project && claude"
```

### Optional: Allow GUI Access

To run Claude Code in Terminal as the sandbox user:

```bash
# Allow the sandbox user to access your display
# Add to your main user's ~/.zshrc:
export DISPLAY=:0

# Grant terminal access in System Preferences > Privacy & Security > Accessibility
```

## Linux Setup

### Create the User

```bash
# Create user with home directory
sudo useradd -m -s /bin/bash claude-sandbox

# Set a password
sudo passwd claude-sandbox
```

### Install Claude Code for the Sandbox User

```bash
# Switch to the sandbox user
sudo -u claude-sandbox -i

# Install Claude Code
curl -fsSL https://claude.ai/install.sh | sh

# Authenticate with Anthropic
claude auth login

# Exit back to your user
exit
```

### Share a Project Directory

```bash
# Option 1: Add both users to a common group
sudo groupadd claude-projects
sudo usermod -aG claude-projects $USER
sudo usermod -aG claude-projects claude-sandbox

# Set group ownership on project
sudo chgrp -R claude-projects /path/to/project
chmod -R g+rwX /path/to/project
chmod g+s /path/to/project  # New files inherit group

# Option 2: Use ACLs
sudo setfacl -R -m u:claude-sandbox:rwX /path/to/project
sudo setfacl -R -d -m u:claude-sandbox:rwX /path/to/project  # Default for new files
```

### Run Claude Code

```bash
# Switch to sandbox user and run claude
sudo -u claude-sandbox -i sh -c "cd /path/to/project && claude"

# Or use su
su - claude-sandbox -c "cd /path/to/project && claude"
```

### Optional: Restrict Network Access

Use iptables to limit what the sandbox user can access:

```bash
# Allow only HTTPS to Anthropic API
sudo iptables -A OUTPUT -m owner --uid-owner claude-sandbox -p tcp --dport 443 -d api.anthropic.com -j ACCEPT
sudo iptables -A OUTPUT -m owner --uid-owner claude-sandbox -p tcp --dport 443 -d claude.ai -j ACCEPT

# Allow DNS
sudo iptables -A OUTPUT -m owner --uid-owner claude-sandbox -p udp --dport 53 -j ACCEPT

# Block everything else for this user
sudo iptables -A OUTPUT -m owner --uid-owner claude-sandbox -j DROP
```

## Convenience Script

Create a wrapper script to easily run Claude in the sandbox:

```bash
#!/bin/bash
# Save as ~/bin/claude-sandbox

PROJECT_DIR="${1:-.}"
cd "$PROJECT_DIR" || exit 1

sudo -u claude-sandbox -i sh -c "cd $(pwd) && claude"
```

Usage:
```bash
claude-sandbox /path/to/project
```

## Cleanup

### macOS

```bash
# Delete the user and home directory
sudo dscl . -delete /Users/claude-sandbox
sudo rm -rf /Users/claude-sandbox
```

### Linux

```bash
# Delete user and home directory
sudo userdel -r claude-sandbox

# Remove from groups
sudo groupdel claude-projects  # if created
```

## Security Considerations

- The sandbox user shares the same kernel as your main user
- Root exploits could escape the sandbox
- For higher security, combine with container isolation
- Consider using `firejail` on Linux for additional restrictions
