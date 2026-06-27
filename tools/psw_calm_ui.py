"""
Calm terminal output for Personal Security Walkthrough tools.

Stdlib only. Muted cyan/amber palette when stdout is a TTY — no alarm red.
Designed to feel grounded during stressful investigations, not gamified.
"""

from __future__ import annotations

import sys
from typing import TextIO

# Truecolor-ish ANSI (works on Windows Terminal, Git Bash, most modern consoles)
_RESET = "\033[0m"
_DIM = "\033[2m"
_CYAN = "\033[38;2;0;206;209m"
_AMBER = "\033[38;2;212;165;116m"
_GREEN = "\033[38;2;143;188;143m"
_PARCHMENT = "\033[38;2;232;217;194m"
_PANEL = "\033[38;2;45;55;50m"


def _use_color(stream: TextIO | None = None) -> bool:
    stream = stream or sys.stdout
    return hasattr(stream, "isatty") and stream.isatty()


def _c(text: str, code: str, stream: TextIO | None = None) -> str:
    if not _use_color(stream):
        return text
    return f"{code}{text}{_RESET}"


def banner(title: str, subtitle: str = "", stream: TextIO | None = None) -> None:
    stream = stream or sys.stdout
    line = "─" * max(40, len(title) + 4)
    print(_c(line, _PANEL, stream), file=stream)
    print(_c(f"  {title}", _CYAN, stream), file=stream)
    if subtitle:
        print(_c(f"  {subtitle}", _DIM, stream), file=stream)
    print(_c(line, _PANEL, stream), file=stream)


def step(current: int, total: int, message: str, stream: TextIO | None = None) -> None:
    stream = stream or sys.stdout
    label = _c(f"[{current}/{total}]", _CYAN, stream)
    print(f"{label} {message}", file=stream)


def info(message: str, stream: TextIO | None = None) -> None:
    stream = stream or sys.stdout
    print(f"{_c('·', _CYAN, stream)} {message}", file=stream)


def ok(message: str, stream: TextIO | None = None) -> None:
    stream = stream or sys.stdout
    print(f"{_c('✓', _GREEN, stream)} {message}", file=stream)


def warn(message: str, stream: TextIO | None = None) -> None:
    stream = stream or sys.stdout
    print(f"{_c('!', _AMBER, stream)} {message}", file=stream)


def panel(body: str, stream: TextIO | None = None) -> None:
    stream = stream or sys.stdout
    for line in body.splitlines():
        print(f"  {_c('│', _PANEL, stream)} {line}", file=stream)