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
