"""FastAPI application entry point."""

from fastapi import FastAPI

from app.routers.items import router as items_router

app = FastAPI(title="Items Service")
app.include_router(items_router)
