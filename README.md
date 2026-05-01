# Context Engineering: FastAPI Items Service

This repository is a small, realistic FastAPI project built for teaching context engineering in Python codebases.

It is intentionally simple in domain (an in-memory "items" API) but structured like a real project, with routing, models, storage, tests, and quality gates.

## Who This Is For

This repo is for students who:

- already know core Python
- are comfortable reading API code
- are using AI tools to understand, change, and maintain codebases

## Learning Goals

By working in this project, you can practice how to give AI assistants better context across:

1. Domain context (what the app is supposed to do)
2. Repo reality (how dependencies and tooling actually work here)
3. Coding conventions (style, typing, FastAPI patterns)
4. Project structure and architecture (where code lives and why)
5. Quality gates (tests, linting, type checks)
6. Constraints and context hygiene (what not to add, what to ignore)

## What the API Does

The app manages `Item` objects in memory.

Each item has:

- `id: int`
- `name: str`
- `description: str | None`

Endpoints:

- `GET /items/` - list all items
- `POST /items/` - create an item
- `GET /items/{item_id}` - get one item by ID (returns `404` if missing)

## Project Layout

```text
app/
  __init__.py
  main.py
  models.py
  storage.py
  routers/
    __init__.py
    items.py
tests/
  test_items.py
pyproject.toml
uv.lock
AGENTS.md
```

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Quick Start

From the project root:

```bash
uv run python -V
uv run uvicorn app.main:app --reload
```

Open:

- API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Note: `/` is not defined in this project, so visiting the root URL returns `404` by design.

## Quality Gates

Run these from the project root:

```bash
uv run pytest
uv run ruff check app tests
uv run mypy app
```

Expected result: tests pass, lint is clean, and mypy reports no type errors.

## Why In-Memory Storage?

This project deliberately avoids databases and ORMs so students can focus on:

- code reading and navigation
- architecture awareness
- safe, incremental edits with AI assistance
- test-driven verification loops

## Suggested Student Workflow

1. Read endpoint behavior in `app/routers/items.py`.
2. Trace model and storage usage through `app/models.py` and `app/storage.py`.
3. Run tests before making changes.
4. Make one small change.
5. Re-run tests/lint/types.
6. Reflect on what context the AI needed (or missed).

## Constraints for Exercises

Unless an exercise says otherwise:

- keep storage in memory (`app/storage.py`)
- do not add database/ORM layers
- keep architecture small and explicit
- prefer clear type hints and readable FastAPI patterns
