<!-- Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817 -->
# Telegram Bot Toolkit - Operational User Manual

This manual provides authoritative guidance for utilizing **`telegram-bot-toolkit`**, the shared zero-dependency formatting, sanitization, message chunking, and financial UI card components library across the Antigravity fleet.

---

## 1. System Overview

`telegram-bot-toolkit` provides pure, high-performance utility functions and formatting engines designed specifically for Telegram bots:
- **MarkdownV2 & HTML Sanitization**: Prevents parse errors (`TelegramError: Can't parse entities`) caused by raw user inputs or financial tickers containing reserved characters (`_`, `*`, `[`, `]`, `(`, `)`, `~`, `` ` ``, `>`, `#`, `+`, `-`, `=`, `|`, `{`, `}`, `.`, `!`).
- **Smart Message Chunking**: Automatically breaks unbounded messages into chunks $\le 4,096$ characters at logical paragraph/newline boundaries.
- **Financial Cards & Unicode Badges**: Generates visual range sliders, multi-factor conviction stars, adaptive price decimals, and signal badges for rich chat UI.

---

## 2. Text Sanitization & Safe Delivery

### 2.1 Escaping MarkdownV2
```python
from telegram_bot_toolkit import escape_markdown

raw_text = "Price: $95,000.50! [BTC] is up +5.2% (1h)."
safe_md = escape_markdown(raw_text, version=2)
# All reserved characters escaped: Price: \$95,000\.50\! \[BTC\] is up \+5\.2\% \(1h\)\.
```

### 2.2 Escaping HTML
```python
from telegram_bot_toolkit import escape_html

raw_text = "BTC > $95k & ETH < $3.5k"
safe_html = escape_html(raw_text)
# BTC &gt; $95k &amp; ETH &lt; $3.5k
```

### 2.3 Safe Message Chunking (4,096-Character Limit)
Telegram strictly limits message bodies to 4,096 UTF-8 characters. `chunk_message` paginates long messages cleanly:
```python
from telegram_bot_toolkit import chunk_message

long_report = "\n".join([...]) # 10,000 characters
chunks = chunk_message(long_report, max_length=4000)

for chunk in chunks:
    await context.bot.send_message(chat_id=chat_id, text=chunk, parse_mode="HTML")
```

---

## 3. Financial UI Components & Visual Cards

### 3.1 Symbol Normalization (`clean_symbol`)
```python
from telegram_bot_toolkit import clean_symbol

clean_symbol("$BTC/USDT")  # "BTC"
clean_symbol("eth/usd")     # "ETH"
clean_symbol("SOL")         # "SOL"
```

### 3.2 Visual Range Sliders (`make_slider`)
Renders an ASCII/Unicode progress slider representing position in a range (e.g. 24h High/Low or RSI):
```python
from telegram_bot_toolkit import make_slider

# Static slider at 50%
slider = make_slider(value=50, min_val=0, max_val=100, width=15)
# Output: [------●-------]

# Dynamic slider with positive 24h change
slider_up = make_slider(value=75, min_val=0, max_val=100, change_24h=5.2)
# Output: [----------►---]
```

### 3.3 Signal Badges & Emojis (`format_signal`)
```python
from telegram_bot_toolkit import format_signal

format_signal("BUY")          # "🟢 BUY"
format_signal("STRONG BUY")   # "🟢 STRONG BUY"
format_signal("SELL")         # "🔴 SELL"
format_signal("HOLD")         # "⚪ HOLD"
format_signal("TAKE PROFIT")  # "🎯 TAKE PROFIT"
```

### 3.4 Adaptive Price & Momentum Formatting
```python
from telegram_bot_toolkit import format_price, format_price_momentum

format_price(95123.456)             # "$95,123.46"
format_price(0.00004523)           # "$0.00004523" (adaptive decimal scaling)
format_price_momentum(95000, 5.2)  # "$95,000.00 ▲ +5.20%"
```

### 3.5 Conviction Score & Stars (`calculate_conviction_score`)
```python
from telegram_bot_toolkit import calculate_conviction_score

stars, label = calculate_conviction_score(
    signal_type="BUY",
    rsi=52.0,
    macd_hist=15.0,
    vol_ratio=2.1,
)
# stars: 5 (⭐⭐⭐⭐⭐)
# label: "High Conviction Breakout"
```

---

## 4. Verification & Testing

Run unit tests via `pytest`:
```bash
python3 -m pytest tests/
```
Output:
```
============================== 11 passed in 0.01s ==============================
```
