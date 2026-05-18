# AGENTS.md

## Purpose

This repository owns the versioned HTTP protocol schemas shared by JQAnywhere and the MiniQMT agent.

## Commands

- Create a virtualenv with `python -m venv .venv`.
- Install for development with `.venv/bin/python -m pip install -e ".[dev]"`.
- Format with `.venv/bin/ruff format .`.
- Lint with `.venv/bin/ruff check .`.
- Test with `.venv/bin/pytest`.

## Constraints

- Keep this package free of `xtquant`, FastAPI, broker, and JQAnywhere runtime dependencies.
- Pydantic models in `miniqmt_protocol.models` are the compatibility contract; avoid breaking field names without a version bump.
- Use explicit enums/literals for request methods and statuses where practical.
- Prefer additive schema changes over breaking changes.
