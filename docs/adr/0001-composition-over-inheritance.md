<!-- Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817 -->
# ADR 0001: Adoption of Clean Architecture and Strict Composition Over Inheritance

## Status
Accepted

## Context
To prevent architectural drift, fragile base classes, and tightly coupled systems across **Telegram Bot UI Toolkit**, a disciplined architectural foundation was required.

## Decision
1. **Ports & Adapters**: Decouple domain entities from frameworks, network protocols, and storage drivers.
2. **Composition Over Inheritance**: Forbid deep inheritance hierarchies. Assemble capabilities via dependency injection and strategy composition.
3. **Strongly-Typed Contracts**: Enforce strict interface and event definitions.

## Consequences
- **Positive**: Subsystems can be tested in 100% isolation; clean lifecycle and high maintainability.
- **Negative**: Requires explicit dependency wiring at initialization.
