# CATALOG.md - telegram-bot-toolkit
<!-- Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817 -->

| File Name | Purpose | Inputs | Outputs |
| :--- | :--- | :--- | :--- |
| `src/telegram_bot_toolkit/__init__.py` | Package root exposing public formatting & sanitization API | N/A | Public function exports |
| `src/telegram_bot_toolkit/sanitization.py` | Telegram MarkdownV2/HTML sanitization & chunking | Raw text, max character chunk limit | Escaped strings, list of safe chunks |
| `src/telegram_bot_toolkit/cards.py` | UI presentation widgets (sliders, badges, RSI, volume, conviction) | Metrics (price, volume, RSI, MACD, signals) | Formatted Telegram text lines & widgets |
| `tests/test_toolkit.py` | Unit tests for sanitization, chunking, and presentation formatters | Test suites | Pytest results (11 passed) |
| `pyproject.toml` | PEP 621 build specification and package metadata | Packaging config | Installable wheel/editable package |

## Standardized Architecture & Governance Documentation (`docs/`)

| File | Description | Inputs | Outputs |
| :--- | :--- | :--- | :--- |
| `docs/domain/DOMAIN_MODEL.md` | Authoritative OOA domain model specification defining entities, value objects, CRC matrix, and invariants. | Source code | Pure domain model |
| `docs/architecture/OBJECT_TOPOLOGY.md` | Authoritative OOD/SAD system architecture document specifying component topology, actors, and patterns. | Actor mesh & core modules | Architecture specification |
| `docs/contracts/INTERFACES_AND_EVENTS.md` | OOP contracts, protocols, event catalog, and dynamic interaction diagrams. | Event bus & protocols | Interface contracts |
| `docs/adr/0001-composition-over-inheritance.md` | ADR documenting Clean Architecture and composition over inheritance. | Architecture review | Accepted decision |
| `docs/operations/RUNBOOK.md` | Operational runbook detailing bootstrap, configuration, lifecycle commands, and troubleshooting. | Scripts & runbooks | Operations guide |
| `docs/USER_MANUAL.md` | Authoritative operational user manual for developers, operators, and bots. | API specifications | User guide |
