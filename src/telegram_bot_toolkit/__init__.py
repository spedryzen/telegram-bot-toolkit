# Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817
__version__ = "1.1.0"
"""
Telegram Bot Toolkit.

Shared utilities for Telegram bot development:
- MarkdownV2 and HTML entity sanitization
- 4,096-character safe message pagination / chunking
- Unicode range sliders, badges, and financial card formatters
"""

from .sanitization import (
    escape_markdown,
    escape_html,
    chunk_message,
)

from .cards import (
    clean_symbol,
    make_slider,
    get_momentum_arrows,
    format_price,
    format_price_adaptive,
    format_price_momentum,
    format_signal,
    format_volume,
    format_rsi,
    calculate_conviction_score,
    format_lite_reasoning,
)

__all__ = [
    "escape_markdown",
    "escape_html",
    "chunk_message",
    "clean_symbol",
    "make_slider",
    "get_momentum_arrows",
    "format_price",
    "format_price_adaptive",
    "format_price_momentum",
    "format_signal",
    "format_volume",
    "format_rsi",
    "calculate_conviction_score",
    "format_lite_reasoning",
]
