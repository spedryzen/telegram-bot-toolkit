
## [2026-09-26] - Docs & Governance: Retroactive OOA/OOD/OOP Documentation Synthesis & Architecture Baseline
- **Timestamp**: 2026-09-26T01:25:00-07:00 (PDT)
- **Modified files**:
  - `docs/domain/DOMAIN_MODEL.md`
  - `docs/architecture/OBJECT_TOPOLOGY.md`
  - `docs/contracts/INTERFACES_AND_EVENTS.md`
  - `docs/adr/0001-composition-over-inheritance.md`
  - `docs/operations/RUNBOOK.md`
- **Summary**: Synthesized authoritative OOA/OOD/OOP documentation suite and operational runbook adhering to system-wide governance directives.
- **Impact**: Zero architectural drift, standardized documentation parity across workstation repositories.

# CHANGELOG.md - telegram-bot-toolkit
## [1.0.1] - 2026-09-14
- **Timestamp**: 2026-09-14T04:24:56-0700 (PDT)
- **Summary**: Consolidate fleet governance, automated process watchdog, and stress-tested risk simulation
- **Reason**: Automated fleet version bump.
- **Impact**: Release artifact ready for distribution.

<!-- Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817 -->

## [0.1.1] - 2026-09-14 02:14:00 PDT
- **Modified files**: `src/telegram_bot_toolkit/cards.py`, `.gitignore`
- **Summary**: Harmonized `format_price_momentum` badge structure to display directional momentum badges (`▲`, `▼`, `🔥`, `🩸`) compatible with both legacy `momentum-sniper` and `crypto-signals` formatting assertions. Added project `.gitignore`.
- **Reason**: Option A cross-project consolidation compatibility.
- **Impact**: 100% test compatibility across all consumer bot test suites.

## [0.1.0] - 2026-09-14 01:37:00 PDT
- **Modified files**: Initial package creation (`src/`, `tests/`, `pyproject.toml`, `setup.py`, `README.md`, `CATALOG.md`).
- **Summary**: Extracted Telegram UI presentation formatters, MarkdownV2/HTML sanitization, and 4,096-char message chunking from `momentum-sniper` and `crypto-signals`.
- **Reason**: Cross-project code consolidation and deduplication (Phase 2 / Option 1).
- **Impact**: Provides reusable, standalone formatting utilities for all Telegram trading and alerting bots.
