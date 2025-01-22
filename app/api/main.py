"""This file registers application routers"""

from fastapi import APIRouter
from app.api.routers import items

router = APIRouter()

# Include the items router
router.include_router(items.router, prefix='/items', tags=['items'])
