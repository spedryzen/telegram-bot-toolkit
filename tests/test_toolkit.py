# Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817
"""Unit tests for telegram_bot_toolkit sanitization, chunking, and cards."""

import pytest
from telegram_bot_toolkit import (
    escape_markdown,
    escape_html,
    chunk_message,
    clean_symbol,
    make_slider,
    get_momentum_arrows,
    format_price,
    format_price_momentum,
    format_signal,
    format_volume,
    format_rsi,
    calculate_conviction_score,
    format_lite_reasoning,
)


def test_escape_markdown():
    raw = "Hello *world*! Price: $100.50 [Link](http://example.com) - Note_1"
    escaped = escape_markdown(raw, version=2)
    assert "\\*" in escaped
    assert "\\!" in escaped
    assert "\\." in escaped
    assert "\\-" in escaped
    assert "\\_" in escaped


def test_escape_html():
    raw = "<b>Hello</b> & <welcome>"
    escaped = escape_html(raw)
    assert "&lt;b&gt;" in escaped
    assert "&amp;" in escaped


def test_chunk_message_short():
    msg = "Short message"
    chunks = chunk_message(msg, max_length=100)
    assert len(chunks) == 1
    assert chunks[0] == msg


def test_chunk_message_long_splits_at_newline():
    lines = [f"Line {i} content text" for i in range(50)]
    msg = "\n".join(lines)
    chunks = chunk_message(msg, max_length=200)
    assert len(chunks) > 1
    for c in chunks:
        assert len(c) <= 200
    # Recombined contains all lines
    recombined = "\n".join(chunks)
    for line in lines:
        assert line in recombined


def test_clean_symbol():
    assert clean_symbol("$BTC/USDT") == "BTC"
    assert clean_symbol("eth/usdc") == "ETH"
    assert clean_symbol("SOL") == "SOL"


def test_make_slider():
    slider = make_slider(50, 0, 100, width=15)
    assert len(slider) == 17  # 15 chars + [ and ]
    assert slider.startswith("[") and slider.endswith("]")
    assert "●" in slider

    # With positive change
    slider_up = make_slider(75, 0, 100, change_24h=5.2)
    assert "►" in slider_up


def test_format_signal():
    assert "🟢" in format_signal("BUY")
    assert "🔴" in format_signal("SELL")
    assert "⚪" in format_signal("HOLD")
    assert "🎯" in format_signal("TAKE PROFIT")


def test_format_volume():
    assert "📈" in format_volume(1500, 1000)
    assert "📉" in format_volume(800, 1000)


def test_format_rsi():
    assert "🔴" in format_rsi(75.5)
    assert "🟢" in format_rsi(24.0)
    assert "⚪" in format_rsi(50.0)


def test_calculate_conviction_score():
    stars, label = calculate_conviction_score("BUY", rsi=50, macd_hist=10, vol_ratio=2.0)
    assert stars >= 4
    assert isinstance(label, str)


def test_format_lite_reasoning():
    reason = format_lite_reasoning("BUY", rsi=55, macd_hist=5, vol_ratio=1.6, reasoning=[])
    assert "positive" in reason.lower()
