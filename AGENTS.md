real-python-content-engineering

Initial prompt

You are helping me build a small but realistic FastAPI project that I will use to teach context engineering for Python codebases.

## Goal

Create a minimal FastAPI “Items” service with:

- A real project layout (multiple files, not just main.py)
- In-memory storage (no database)
- A couple of tests
- Tooling hooks (ruff, mypy, pytest) so we can talk about “quality gates”

Use the following 6 context categories to guide your design:
1) Domain Context
2) Repo Reality
3) Coding Conventions
4) Project Structure and Architecture
5) Quality Gates
6) Constraints + Context Hygiene

## 1) Domain Context

- The app manages simple “items”.
- Each item has:
  - id: int
  - name: str
  - description: optional str
- The API should support:
  - List all items
  - Create a new item
  - Get an item by id
- If an item does not exist, GET by id should return a 404 with a clear message.

## 2) Repo Reality

- Python version: 3.11+
- Framework: FastAPI
- ASGI server: uvicorn (for local dev)
- Dependency manager: uv (you can assume I’ll run commands like `uv run pytest`)

Create a `pyproject.toml` that includes at least:
- fastapi
- uvicorn[standard]
- pytest
- httpx or fastapi[testclient] (for tests)
- ruff
- mypy

## 3) Coding Conventions

- Follow PEP 8
- Use type hints everywhere (functions, FastAPI endpoints, storage helpers).
- Use Pydantic models for request/response bodies.
- Use snake_case for variables and functions.
- Use idiomatic FastAPI patterns:
  - `HTTPException` for 404s
  - Response models for endpoints
- Keep the code easy for intermediate students to read:
  - No advanced metaprogramming
  - No fancy dependency injection tricks beyond basic imports

## 4) Project Structure and Architecture

Create a small but realistic layout like this:

- `app/`
  - `__init__.py`
  - `main.py`          # creates FastAPI app and includes routers
  - `models.py`        # Pydantic models (Item)
  - `storage.py`       # in-memory “database” functions
  - `routers/`
    - `__init__.py`
    - `items.py`       # /items endpoints live here
- `tests/`
  - `test_items.py`    # a couple of pytest tests for the API
- `pyproject.toml`
- `AGENTS.md`          # leave a placeholder section I can fill in later

Architectural expectations:

- `app.main`:
  - defines `app = FastAPI(...)`
  - includes the `items` router

- `app.models`:
  - define an `Item` Pydantic model with fields: id, name, description | None

- `app.storage`:
  - in-memory dict to hold items
  - functions:
    - `list_items() -> list[Item]`
    - `get_item(item_id: int) -> Item | None`
    - `save_item(item: Item) -> None`

- `app.routers.items`:
  - Router with prefix `/items` and tag `["items"]`
  - Endpoints:
    - `GET /items/` -> list[Item]
    - `GET /items/{item_id}` -> Item or 404
    - `POST /items/` -> create item, return 201 with Item body

## 5) Quality Gates

Set up the project so that I can run:

- `uv run pytest` to run tests
- `uv run ruff check app tests` for linting
- `uv run mypy app` for type checking

Please:
- Add at least 2–3 tests in `tests/test_items.py` using `TestClient`:
  - create an item then read it back
  - reading a missing item returns 404
- Make sure the code you generate is:
  - mypy-clean (no type errors)
  - ruff-clean (no obvious lint issues, using default config)

## 6) Constraints + Context Hygiene

Constraints:

- Do NOT add any database or ORM (no SQLAlchemy, no migrations).
- Keep everything in memory via `app.storage`.
- Keep the layout small and focused; no extra layers like “services” or “repositories”.
- Keep configuration minimal; no env var config systems, no settings classes.

Context hygiene:

- Assume this repo is ONLY for this tutorial.
- Do not introduce extra example files, notebooks, or docs beyond:
  - `AGENTS.md` (you can put a short placeholder section “to be filled by later”)
- Do not generate `.venv` or .env files.

## What to output

Please:

1. Show me the full file tree you propose.
2. Then, for each file, give the complete code:
   - `pyproject.toml`
   - `app/main.py`
   - `app/models.py`
   - `app/storage.py`
   - `app/routers/items.py`
   - `tests/test_items.py`
   - `AGENTS.md` with a short placeholder section like “This will be filled with context-engineering instructions later.”

Make sure the code is ready to be copied into a fresh repo and run with `uv` + `fastapi` + `pytest`.