<!-- Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817 -->
# Telegram Bot UI Toolkit - Operational Runbook

This document provides the operational execution, local bootstrap, process management, and troubleshooting protocols for **Telegram Bot UI Toolkit**.

---

## 1. Runtime Specifications

- **Workstation**: Apple Silicon M4 Mac Studio (36GB RAM, macOS).
- **Process Supervisor**: `pip install -e .`
- **Active Time Zone**: `PST / America/Los_Angeles` (Authoritative across all user-facing displays and logs).
- **Network Ports / Bindings**: `Library`

---

## 2. Environment Configuration

Populate the required environment variables before initialization:
```bash
Consuming library
```

---

## 3. Service Lifecycle Management

```bash
# Start service
pip install -e . start

# Check status
pip install -e . status

# Tail logs
pip install -e . logs

# Graceful stop
pip install -e . stop
```

---

## 4. Health Checks & Troubleshooting Protocols

1. Verify process vitality using `pip install -e . status`.
2. Inspect log files for unhandled exceptions or error events.
3. Verify local port availability before starting services.
