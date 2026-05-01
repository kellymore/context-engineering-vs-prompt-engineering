"""Items API routes."""

from fastapi import APIRouter, HTTPException, status

from app.models import Item
from app.storage import get_item, list_items, save_item

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=list[Item])
def read_items() -> list[Item]:
    """List all items."""
    return list_items()


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int) -> Item:
    """Get one item by id or return 404."""
    item = get_item(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} was not found.",
        )
    return item


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item) -> Item:
    """Create a new item."""
    save_item(item)
    return item
