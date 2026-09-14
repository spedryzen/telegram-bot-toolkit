# CATALOG.md - telegram-bot-toolkit
<!-- Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817 -->

| File Name | Purpose | Inputs | Outputs |
| :--- | :--- | :--- | :--- |
| `src/telegram_bot_toolkit/__init__.py` | Package root exposing public formatting & sanitization API | N/A | Public function exports |
| `src/telegram_bot_toolkit/sanitization.py` | Telegram MarkdownV2/HTML sanitization & chunking | Raw text, max character chunk limit | Escaped strings, list of safe chunks |
| `src/telegram_bot_toolkit/cards.py` | UI presentation widgets (sliders, badges, RSI, volume, conviction) | Metrics (price, volume, RSI, MACD, signals) | Formatted Telegram text lines & widgets |
| `tests/test_toolkit.py` | Unit tests for sanitization, chunking, and presentation formatters | Test suites | Pytest results (11 passed) |
| `pyproject.toml` | Build specification and package metadata | Packaging config | Installable wheel/editable package |
| `setup.py` | Setuptools shim for backwards compatibility | Packaging config | Editable installs (`pip install -e .`) |
