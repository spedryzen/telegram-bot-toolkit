<!-- Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817 -->
# CHANGELOG.md - telegram-bot-toolkit

## [1.1.0] - 2026-10-09
- **Timestamp**: 2026-10-09T11:40:00-07:00 (PDT)
- **Modified files**:
  - `pyproject.toml` (bumped to 1.1.0, added testpaths configuration)
  - `src/telegram_bot_toolkit/__init__.py` (bumped to 1.1.0)
  - `docs/USER_MANUAL.md` (authored comprehensive operational user manual)
  - `CATALOG.md`
  - `CHANGELOG.md`
- **Removed files**:
  - `setup.py` (redundant legacy shim removed in favor of PEP 621 `pyproject.toml`)
- **Summary**:
  - Modernized package configuration to PEP 621 standards, removing obsolete `setup.py`.
  - Authored comprehensive operational user manual [`docs/USER_MANUAL.md`](docs/USER_MANUAL.md).
  - Verified 11/11 tests passing (100% pass rate).
- **Reason**: Clean Architecture modernization, eliminate documentation drift, and maintain parity across the Antigravity fleet.
- **Impact**: Zero-dependency Telegram formatting and sanitization toolkit with PEP 621 compliance.

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

## [1.0.1] - 2026-09-14
- **Timestamp**: 2026-09-14T04:24:56-0700 (PDT)
- **Summary**: Consolidate fleet governance, automated process watchdog, and stress-tested risk simulation
- **Reason**: Automated fleet version bump.
- **Impact**: Release artifact ready for distribution.

## [0.1.1] - 2026-09-14 02:14:00 PDT
- **Modified files**: `src/telegram_bot_toolkit/cards.py`, `.gitignore`
- **Summary**: Harmonized `format_price_momentum` badge structure to display directional momentum badges (`▲`, `▼`, `🔥`, `🩸`) compatible with both legacy `momentum-sniper` and `crypto-signals` formatting assertions. Added project `.gitignore`.
- **Reason**: Option A cross-project consolidation compatibility.
- **Impact**: 100% test compatibility across all consumer bot test suites.

## [0.1.0] - 2026-09-14 01:37:00 PDT
- **Modified files**: Initial package creation (`src/`, `tests/`, `pyproject.toml`, `setup.py`, `README.md`, `CATALOG.md`).
- **Summary**: Extracted Telegram UI presentation formatters, MarkdownV2/HTML sanitization, and 4,096-char message chunking from `momentum-sniper` and `crypto-signals`.
- **Reason**: Standardize presentation layer across fleet bot repositories.
- **Impact**: Clean decoupling of UI cards from quantitative core.
