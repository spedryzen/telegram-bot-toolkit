# Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817
"""
Reusable visual UI widgets, cards, and formatting helpers for Telegram bots.

Provides standardized ASCII range sliders, momentum badges, volume indicators,
RSI visual statuses, conviction star ratings, and symbol cleaning.
"""

from typing import Optional, Tuple, List


def clean_symbol(symbol: str) -> str:
    """
    Sanitizes and normalizes a cryptocurrency symbol string.

    Args:
        symbol: Input trading symbol (e.g. '$BTC/USDT', 'btc', 'BTC/USDC').

    Returns:
        Cleaned, uppercase base symbol (e.g. 'BTC').
    """
    s = symbol.upper().strip().lstrip("$").lstrip("/")
    for suffix in ["/USDT", "/USDC", "/USD", "USDT", "USDC", "USD"]:
        if s.endswith(suffix) and len(s) > len(suffix):
            s = s[:-len(suffix)]
            break
    return s


def make_slider(
    current: float,
    low: float,
    high: float,
    change_24h: Optional[float] = None,
    width: int = 15
) -> str:
    """
    Creates a visual slider string representing current price position within low-high 24h range.

    Example: [───►──────────] or [───●──────────]

    Args:
        current: Current market price.
        low: 24h low price.
        high: 24h high price.
        change_24h: Optional 24h percentage change (adds directional arrow if provided).
        width: Character width of slider bar.

    Returns:
        Formatted ASCII slider string.
    """
    if high <= low:
        ratio = 0.5
    else:
        ratio = (current - low) / (high - low)
        ratio = max(0.0, min(1.0, ratio))
    pos = int(round(ratio * (width - 1)))
    slider_chars = ["─"] * width

    marker = "●"
    if change_24h is not None:
        if change_24h > 0:
            marker = "►"
        elif change_24h < 0:
            marker = "◄"

    slider_chars[pos] = marker
    return f"[{''.join(slider_chars)}]"


def get_momentum_arrows(change_24h: Optional[float]) -> str:
    """
    Returns directional arrows based on 24h percentage change magnitude.

    Args:
        change_24h: 24h price change percentage.

    Returns:
        String of 1, 2, or 3 arrows indicating magnitude and direction.
    """
    if change_24h is None:
        return ""
    abs_change = abs(change_24h)
    if change_24h >= 0:
        if abs_change >= 8.0:
            return "▶▶▶"
        elif abs_change >= 3.0:
            return "▶▶"
        else:
            return "▶"
    else:
        if abs_change >= 8.0:
            return "◀◀◀"
        elif abs_change >= 3.0:
            return "◀◀"
        else:
            return "◀"


def format_price_adaptive(val: float) -> str:
    """
    Formats numerical prices dynamically to preserve significant digits without trailing noise.

    Args:
        val: Numerical price value.

    Returns:
        Formatted price string.
    """
    abs_val = abs(val)
    if abs_val < 0.01:
        s = f"{abs_val:.8f}"
        return s.rstrip("0").rstrip(".") if "." in s else s
    elif abs_val < 1.0:
        return f"{abs_val:.4f}"
    return f"{abs_val:,.2f}"


# Alias for compatibility
format_price = format_price_adaptive


def format_price_momentum(price: float, change_24h: Optional[float]) -> str:
    """
    Formats price with dynamic momentum badge and dollar change.

    Args:
        price: Current price.
        change_24h: 24h price change percentage.

    Returns:
        Formatted price string with emoji and badge.
    """
    if change_24h is None:
        change_24h = 0.0

    dollar_change = price - (price / (1 + (change_24h / 100)))
    dollar_str = f"{'+' if dollar_change >= 0 else '-'}${format_price(dollar_change)}"
    arrows = get_momentum_arrows(change_24h)

    arrow_part = f" {arrows}" if arrows else ""
    if change_24h >= 5.0:
        icon = "🟢"
        badge = f"[🔥 {dollar_str} | {change_24h:+.2f}%{arrow_part}]"
    elif change_24h >= 0.0:
        icon = "🟢"
        badge = f"[{dollar_str} ▲ | {change_24h:+.2f}%{arrow_part}]"
    elif change_24h > -5.0:
        icon = "🔴"
        badge = f"[{dollar_str} ▼ | {change_24h:+.2f}%{arrow_part}]"
    else:
        icon = "🔴"
        badge = f"[🩸 {dollar_str} | {change_24h:+.2f}%{arrow_part}]"

    return f"{icon} ${format_price(price)} {badge}"


def format_signal(signal: str) -> str:
    """
    Formats a signal string with a color-coded emoji indicator.
    🟢 = buy signals, 🔴 = sell signals, ⚪ = hold/neutral, 🎯 = take profit.

    Args:
        signal: Raw signal name (e.g. 'BUY', 'STRONG BUY', 'SELL', 'HOLD').

    Returns:
        Formatted signal string with color emoji.
    """
    s = signal.upper()
    if any(k in s for k in ("BUY",)):
        return f"🟢 {signal}"
    elif any(k in s for k in ("SELL",)):
        return f"🔴 {signal}"
    elif "TAKE PROFIT" in s:
        return f"🎯 {signal}"
    else:
        return f"⚪ {signal}"


def format_volume(vol_curr: float, vol_avg: float) -> str:
    """
    Formats volume with green trend emoji if above average, red if below.

    Args:
        vol_curr: Current period volume.
        vol_avg: Rolling average volume.

    Returns:
        Formatted volume string.
    """
    if vol_avg > 0 and vol_curr > vol_avg:
        pct = (vol_curr / vol_avg) * 100
        return f"📈 ${vol_curr:,.2f} ({pct:.0f}% of avg)"
    elif vol_avg > 0:
        pct = (vol_curr / vol_avg) * 100
        return f"📉 ${vol_curr:,.2f} ({pct:.0f}% of avg)"
    else:
        return f"${vol_curr:,.2f}"


def format_rsi(rsi: Optional[float]) -> str:
    """
    Formats RSI with color-coded emoji.
    🔴 = overbought (>70), 🟢 = oversold (<30), ⚪ = neutral.

    Args:
        rsi: 14-period RSI value.

    Returns:
        Formatted RSI string.
    """
    if rsi is None:
        return "⚪ N/A"
    if rsi >= 70:
        return f"🔴 {rsi:.2f} (Overbought)"
    elif rsi <= 30:
        return f"🟢 {rsi:.2f} (Oversold)"
    else:
        return f"⚪ {rsi:.2f}"


def calculate_conviction_score(
    final_signal: str,
    rsi: Optional[float],
    macd_hist: Optional[float],
    vol_ratio: float
) -> Tuple[int, str]:
    """
    Calculates a 5-Star Conviction score based on signal strength, RSI, MACD, and Volume.

    Args:
        final_signal: Signal string.
        rsi: RSI indicator value.
        macd_hist: MACD histogram value.
        vol_ratio: Current volume / average volume ratio.

    Returns:
        Tuple of (star_count: int, label: str).
    """
    score = 1
    is_buy = "BUY" in final_signal
    is_sell = "SELL" in final_signal
    is_strong = "STRONG" in final_signal

    if is_strong:
        score += 1

    if rsi is not None:
        if is_buy:
            if 40 <= rsi <= 65 or rsi < 30:
                score += 1
        elif is_sell:
            if 35 <= rsi <= 60 or rsi > 70:
                score += 1

    if macd_hist is not None:
        if is_buy and macd_hist > 0:
            score += 1
        elif is_sell and macd_hist < 0:
            score += 1

    if vol_ratio >= 1.5:
        score += 1

    stars = max(1, min(5, score))

    labels = {
        5: "Maximum Conviction",
        4: "High Conviction",
        3: "Moderate Conviction",
        2: "Low Conviction",
        1: "Weak Conviction"
    }

    return stars, labels[stars]


def format_lite_reasoning(
    final_signal: str,
    rsi: Optional[float],
    macd_hist: Optional[float],
    vol_ratio: float,
    reasoning: List[str]
) -> str:
    """
    Formats plain-English explanation for Lite Mode.

    Args:
        final_signal: Signal string.
        rsi: RSI indicator value.
        macd_hist: MACD histogram value.
        vol_ratio: Volume ratio.
        reasoning: List of technical reason strings from SignalEngine.

    Returns:
        Plain-English summary sentence.
    """
    if reasoning:
        if len(reasoning) == 1:
            return reasoning[0]
        return "\n" + "\n".join(reasoning)

    reasons = []
    if "BUY" in final_signal:
        reasons.append("The trend is strongly positive" if "STRONG" in final_signal else "The trend is positive")
        if macd_hist is not None and macd_hist > 0:
            reasons.append("MACD momentum is positive")
        if rsi is not None and (40 <= rsi <= 65):
            reasons.append(f"RSI ({rsi:.1f}) is in healthy buy zone")
        elif rsi is not None and rsi < 30:
            reasons.append(f"RSI ({rsi:.1f}) indicates oversold rebound")
        if vol_ratio >= 1.5:
            reasons.append(f"buying activity is high ({vol_ratio:.1f}x avg volume)")
    elif "SELL" in final_signal:
        reasons.append("The trend is strongly negative" if "STRONG" in final_signal else "The trend is negative")
        if macd_hist is not None and macd_hist < 0:
            reasons.append("MACD momentum is negative")
        if rsi is not None and (35 <= rsi <= 60):
            reasons.append(f"RSI ({rsi:.1f}) shows downward pressure")
        elif rsi is not None and rsi > 70:
            reasons.append(f"RSI ({rsi:.1f}) indicates overbought rejection")
        if vol_ratio >= 1.5:
            reasons.append(f"selling activity is high ({vol_ratio:.1f}x avg volume)")
    else:
        reasons.append("Market is consolidating with neutral technical indicators")

    if reasons:
        return " and ".join(reasons) + "."
    else:
        return "Technical indicators suggest monitoring."


__all__ = [
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
