"""Pydantic models for API request and response bodies."""

from pydantic import BaseModel


class Item(BaseModel):
    """Represents a stored item."""

    id: int
    name: str
    description: str | None = None
