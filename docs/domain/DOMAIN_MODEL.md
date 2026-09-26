<!-- Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817 -->
# Telegram Bot UI Toolkit - Domain Model (OOA Specification)

This document provides the authoritative Object-Oriented Analysis (OOA) specification for **Telegram Bot UI Toolkit**. It defines the core domain boundaries, entity identities, immutable value objects, Class-Responsibility-Collaborator (CRC) matrices, and non-negotiable business invariants.

---

## 1. Domain Boundary & Context

Rich ASCII dashboard, status table, progress bar, and interactive keyboard formatting toolkit for Telegram bots.

The domain is strictly decoupled from external infrastructure drivers, databases, web protocols, and user interfaces in compliance with Clean Architecture (Ports & Adapters).

---

## 2. Core Entities & Value Objects

#### `DashboardLayout`
Structured presentation model for system metrics, gauges, and tables.


---

## 3. Class-Responsibility-Collaborator (CRC) Matrix

| Class / Role Name | Responsibilities (What it Owns & Enforces) | Collaborators (Message Targets) |
| :--- | :--- | :--- |
| **`MessageBuilder`** | Formats rich HTML cards and ASCII gauges for Telegram delivery. | Formatters |

---

## 4. Domain Invariants & Business Rules

1. **All HTML tags must be properly closed to avoid Telegram API parse errors.**

---

## 5. Maintenance Guidance

> [!TIP]
> **Extending Domain Entities**:
> When adding new attributes to domain models, ensure all state invariants are defensively enforced at construction time. Keep value objects immutable and self-validating.
