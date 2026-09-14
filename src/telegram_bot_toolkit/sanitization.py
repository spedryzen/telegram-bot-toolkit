# Copyright (c) 2026 Ed Grant, Email: ed@edgrant.com, Phone: (951) 610-8817
"""
Sanitization and message pagination utilities for Telegram Bot APIs.

Provides escaping for MarkdownV2 and HTML parse modes to eliminate syntax parsing
crashes, as well as line-aware chunking to respect Telegram's 4,096-character limit.
"""

import re
import html
from typing import List

# Characters that must be escaped in Telegram MarkdownV2 outside code blocks:
# '_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!'
_MDV2_ESCAPE_REGEX = re.compile(r"([_*\[\]()~`>#+\-=|{}.!\\])")


def escape_markdown(text: str, version: int = 2) -> str:
    """
    Escapes reserved Markdown characters for safe Telegram transmission.

    Args:
        text: Raw input string.
        version: Markdown version (1 or 2). Defaults to 2 (MarkdownV2).

    Returns:
        Properly escaped string.
    """
    if not text:
        return ""
    if version == 2:
        return _MDV2_ESCAPE_REGEX.sub(r"\\\1", text)
    else:
        # Legacy Markdown V1 escaping
        return re.sub(r"([_*`\\[])", r"\\\1", text)


def escape_html(text: str) -> str:
    """
    Escapes reserved HTML entities for Telegram HTML parse mode.

    Args:
        text: Raw input string.

    Returns:
        HTML-escaped string replacing &, <, > with entities.
    """
    if not text:
        return ""
    return html.escape(text, quote=False)


def chunk_message(text: str, max_length: int = 4096) -> List[str]:
    """
    Splits a long message into multiple chunks that never exceed max_length.
    Prefers splitting on newlines to preserve card and table structure.

    Args:
        text: The message string to send.
        max_length: Maximum allowed characters per chunk (default: 4096).

    Returns:
        List of message chunks ready for sequential dispatch.
    """
    if not text or len(text) <= max_length:
        return [text] if text else []

    chunks = []
    remaining = text

    while len(remaining) > max_length:
        # Look for a newline split point within the allowed window
        split_idx = remaining.rfind("\n", 0, max_length)

        # If no newline found, look for a space
        if split_idx == -1 or split_idx < max_length // 2:
            space_idx = remaining.rfind(" ", 0, max_length)
            if space_idx != -1 and space_idx >= max_length // 2:
                split_idx = space_idx
            else:
                # Hard cut if no clean boundary exists
                split_idx = max_length

        chunk = remaining[:split_idx].strip()
        if chunk:
            chunks.append(chunk)
        remaining = remaining[split_idx:].strip()

    if remaining:
        chunks.append(remaining)

    return chunks


__all__ = ["escape_markdown", "escape_html", "chunk_message"]
