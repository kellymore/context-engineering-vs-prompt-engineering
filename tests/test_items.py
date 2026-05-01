"""API tests for items endpoints."""

from fastapi.testclient import TestClient

from app.main import app
from app.storage import clear_items

client = TestClient(app)


def setup_function() -> None:
    """Reset in-memory storage between tests."""
    clear_items()


def test_create_item_then_read_it_back() -> None:
    """Creating an item makes it available by id."""
    payload = {"id": 1, "name": "Notebook", "description": "Paper notebook"}

    create_response = client.post("/items/", json=payload)
    assert create_response.status_code == 201
    assert create_response.json() == payload

    read_response = client.get("/items/1")
    assert read_response.status_code == 200
    assert read_response.json() == payload


def test_read_missing_item_returns_404() -> None:
    """Reading an unknown item should return a clear 404."""
    response = client.get("/items/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Item with id 999 was not found."}


def test_list_items_returns_all_created_items() -> None:
    """Listing items returns all currently stored items."""
    first_item = {"id": 1, "name": "Notebook", "description": "Paper notebook"}
    second_item = {"id": 2, "name": "Pencil", "description": None}

    client.post("/items/", json=first_item)
    client.post("/items/", json=second_item)

    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == [first_item, second_item]
