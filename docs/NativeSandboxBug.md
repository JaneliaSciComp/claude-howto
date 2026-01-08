# Pixi Sandbox Bug on macOS

## Summary

`pixi install` panics when run inside Claude Code's sandbox on macOS due to blocked access to the SystemConfiguration daemon.

## Error Message

```
thread 'main2' panicked at /Users/runner/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/system-configuration-0.6.1/src/dynamic_store.rs:154:1:
Attempted to create a NULL object.
```

## Root Cause

The sandbox blocks access to a macOS Mach service that `pixi` needs for network operations:

```
(deny mach-lookup (global-name "com.apple.SystemConfiguration.configd"))
```

### Chain of Events

1. `pixi` uses the Rust `system-configuration-rs` crate (v0.6.1) to access macOS network configuration
2. This crate calls `SCDynamicStoreCreate` to connect to the SystemConfiguration daemon via Mach IPC
3. The sandbox blocks the `mach-lookup` call to `com.apple.SystemConfiguration.configd`
4. `SCDynamicStoreCreate` returns `NULL` when the Mach service is unavailable
5. The crate panics instead of handling the `NULL` gracefully (this is a bug in the crate)

### Why It's Needed

Network operations (like downloading packages from conda-forge/PyPI) go through `reqwest`, which uses the SystemConfiguration framework to discover proxy settings and DNS configuration on macOS.

## Workaround

Run `pixi install` outside the sandbox by disabling sandbox mode.

## Fix

The Claude Code sandbox needs to allow this Mach service lookup. The seatbelt rule needed is:

```
(allow mach-lookup (global-name "com.apple.SystemConfiguration.configd"))
```

## Related Issues

- [mullvad/system-configuration-rs#72](https://github.com/mullvad/system-configuration-rs/issues/72) - Crate should handle NULL gracefully instead of panicking
- [astral-sh/uv#16664](https://github.com/astral-sh/uv/issues/16664) - Same issue affects `uv` package manager

## Environment

- macOS (Darwin 24.5.0)
- pixi 0.47.0
- system-configuration crate 0.6.1
