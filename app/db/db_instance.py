from fastapi import Header, Depends
from app.db.connector import PostgresConnector

def get_postgres_connector(env: str = Header(..., alias="env", description="Environment Name"),) -> PostgresConnector:
  return PostgresConnector(env=env)