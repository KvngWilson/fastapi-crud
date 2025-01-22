import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_put_simulation_status_waiting():
  response = client.get("/itemsg/1/", headers={"env": "test"})
  assert response.status_code == 200
  assert response.json() == {"status": "success", "status_code": 200, "message": ""}