# MiniQMT-Protocol

Shared Pydantic schemas for the remote MiniQMT HTTP protocol.

The package is intentionally small and dependency-light so both JQAnywhere and the MiniQMT agent can depend on the same request/response contract.

## Development

```bash
python -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
.venv/bin/pytest
```
