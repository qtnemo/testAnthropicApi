# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A minimal sandbox for experimenting with the Anthropic Python SDK (`anthropic`). Currently contains a single script, `simple_claude_app.py`, that issues a one-shot `messages.create` call against `claude-haiku-4-5` and prints the text blocks from the response.

## Running

```powershell
python simple_claude_app.py
```

The SDK reads the credentials `ANTHROPIC_API_KEY` from the file .env — `anthropic.Anthropic()` is constructed with no explicit key.

## Code Style

- Python (PEP 8):
    - 4-space indent
    - `PascalCase` for classes
    - `snake_case` for functions, methods, variables, parameters
    - `_leading_underscore` for non-public attributes
    - `UPPER_SNAKE_CASE` for module-level constants

## Conventions

- The response is iterated as `response.content` blocks, gated on `block.type == "text"`. Preserve this pattern when adding tool use, thinking, or other block types — don't assume a single text block.
- Model ID is pinned to `claude-haiku-4-5-20251001`. When migrating models, update the string literal directly; there's no config layer.
