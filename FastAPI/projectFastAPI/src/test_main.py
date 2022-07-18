from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from main import app, get_db

import os
if (os.path.exists("test.db")): os.remove("test.db")



SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_store():
    response = client.post(
        "/stores/",
        json={"name": "store1"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "store1"
    
def test_get_store():
    response = client.post(
        "/stores/",
        json={"name": "store2"},
    )
    data = response.json()
    store_id = data["id"]
    response = client.get(f"/store/{store_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "store2"
    assert data["id"] == store_id
    
def test_update_store():
    response = client.post(
        "/stores/",
        json={"name": "store4"},
    )
    data = response.json()
    store_id = data["id"]
    response = client.put(
        f"/store/{store_id}/change",
        params={"name": "store3"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "store3"
    assert data["id"] == store_id
    
def test_delete_store():
    response = client.post(
        "/stores/",
        json={"name": "store4"},
    )
    data = response.json()
    store_id = data["id"]
    response = client.delete(f"/store/{store_id}/delete",)
    assert response.status_code == 200, response.text
    response2 = client.get(f"/store/{store_id}")
    assert response2.status_code == 200, response2.text
    data = response2.json()
    assert data==None