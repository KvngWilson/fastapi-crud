from fastapi import APIRouter, HTTPException, Depends, status, Request
from app.db.connector import PostgresConnector
from app.db.db_instance import get_postgres_connector
from app.core.models import APIResponse

router = APIRouter()

# Simulated in-memory database for items
items_db = {}

@router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=APIResponse,)
async def get_item(item_id: int):
  """Retrieve an item by ID."""
  item = items_db.get(item_id)
  if not item:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found.")
  
  return APIResponse(status="success", status_code=status.HTTP_200_OK, message="Item retrieved successfully.", data=item)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=APIResponse,)

async def create_item(item_id: int, item_data: dict):
  """Create a new item in database."""
  if item_id in items_db:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item already exists.")
  
  items_db[item_id] = item_data
  return APIResponse(status="success", status_code=status.HTTP_201_CREATED, message= "Item created successfully.")

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT,)
async def delete_item(item_id: int):
  """Delete an item by ID."""
  if item_id not in items_db:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found.")
  
  del items_db[item_id]
  return APIResponse(status="success", status_code=status.HTTP_204_NO_CONTENT, message="Item deleted successfully.")