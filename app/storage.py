"""In-memory storage helpers for items."""

from app.models import Item

_items: dict[int, Item] = {}


def list_items() -> list[Item]:
    """Return all currently stored items."""
    return list(_items.values())


def get_item(item_id: int) -> Item | None:
    """Return one item by id, or None when missing."""
    return _items.get(item_id)


def save_item(item: Item) -> None:
    """Save or replace an item in memory."""
    _items[item.id] = item


def clear_items() -> None:
    """Clear in-memory storage, used by tests."""
    _items.clear()
