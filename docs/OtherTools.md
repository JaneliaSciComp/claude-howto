# Other AI Coding Tools

This document covers differences to expect when working with AI coding tools other than Claude Code, including sandboxing considerations.

> [!WARNING]
> This documentation is unvetted and may be out of date by the time you read it.

## Tool Comparison

| Tool | Execution Model | Sandboxing | Network Control |
|------|-----------------|------------|-----------------|
| Claude Code | Local CLI | Native sandbox, containers | Configurable allowlist |
| OpenAI Codex CLI | Local CLI | None built-in | None built-in |
| Google Gemini CLI | Local CLI | None built-in | None built-in |
| GitHub Copilot | Editor plugin | N/A (suggestions only) | N/A |
| Cursor | Editor with agent | Editor-managed | Editor-managed |
| Aider | Local CLI | None built-in | None built-in |

## OpenAI Codex CLI

[Codex CLI](https://github.com/openai/codex) is OpenAI's command-line coding agent.

**Key differences from Claude Code:**
- No built-in sandboxing - runs commands directly on your system
- No network isolation features
- Uses OpenAI API (requires `OPENAI_API_KEY`)

**Sandboxing recommendations:**
- Use the same devcontainer setup as Claude Code
- The firewall script needs modification to allow OpenAI endpoints:
  ```bash
  # Add to ALLOWED_DOMAINS in init-firewall.sh
  "api.openai.com"
  ```

**Running in our devcontainer:**
```bash
# Install Codex CLI
npm install -g @openai/codex

# Set API key
export OPENAI_API_KEY="your-key"

# Run with full auto mode
codex --full-auto
```

## Google Gemini CLI

[Gemini CLI](https://github.com/google-gemini/gemini-cli) is Google's command-line coding agent.

**Key differences from Claude Code:**
- No built-in sandboxing
- No network isolation features
- Uses Google AI API (requires `GEMINI_API_KEY`)

**Sandboxing recommendations:**
- Use the same devcontainer setup as Claude Code
- The firewall script needs modification to allow Google endpoints:
  ```bash
  # Add to ALLOWED_DOMAINS in init-firewall.sh
  "generativelanguage.googleapis.com"
  ```

**Running in our devcontainer:**
```bash
# Install Gemini CLI
npm install -g @anthropic-ai/gemini-cli  # Check actual package name

# Set API key
export GEMINI_API_KEY="your-key"

# Run
gemini
```

## Aider

[Aider](https://github.com/paul-gauthier/aider) is a popular open-source AI pair programming tool that works with multiple LLM backends.

**Key differences from Claude Code:**
- Supports multiple backends (OpenAI, Anthropic, local models)
- No built-in sandboxing
- Python-based (install via pip)

**Sandboxing recommendations:**
- Use the same devcontainer setup
- Add appropriate API endpoints to firewall based on which backend you use

**Running in our devcontainer:**
```bash
# Install via pixi/pip
pip install aider-chat

# Run with Claude backend
export ANTHROPIC_API_KEY="your-key"
aider --model claude-3-5-sonnet
```

## Common Sandboxing Strategy

All these tools can run in our devcontainer with the same isolation benefits:

1. **Filesystem isolation**: Tools can only access mounted directories
2. **Network isolation**: iptables restricts outbound traffic to allowed domains
3. **Reproducibility**: Same environment across team members
4. **Easy reset**: Delete container and rebuild for clean state

To add a new tool:
1. Add its API endpoint to `.devcontainer/init-firewall.sh`
2. Install the tool in the container (modify Dockerfile or install at runtime)
3. Set appropriate API keys as environment variables

## Security Considerations

| Concern | Claude Code | Other Tools |
|---------|-------------|-------------|
| Permission prompts | Yes (can disable) | Usually no |
| Audit logging | Built-in | Varies |
| Command confirmation | Configurable | Varies |
| File change review | Built-in | Varies |

When using tools without built-in safety features, the container sandbox becomes even more important as your primary defense layer.
