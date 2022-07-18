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



def test_route():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "This is the best API ever made!"}


# Create Tests
def test_create_shopping():
    response = client.post('/shoppings/', json= {"id": 1, "name": "Braga Parque", "address": "Braga"})
    assert response.status_code == 200
    
    data_response = response.json()
    
    
    assert data_response["name"] == "Braga Parque"


# Read Tests
def test_read_shopping():
    name = "Nova Arcada"
    address = "Braga"
    response = client.post('/shoppings/', json={"id": 2, "name": name, "address": address})

    data = response.json()
    shopping_id = data["id"]

    response = client.get(f'/shoppings/{shopping_id}/')
    data_response = response.json()

    assert response.status_code == 200
    assert data_response["id"] == 2
    assert data_response["name"] == name
    assert data_response["address"] == address


# Update Tests
def test_update_shopping_name():
    name = "Colombo"
    address = "Lisboa"
    response = client.post('/shoppings/', json={"id": 3, "name": name, "address": address})
    
    data = response.json()
    shopping_id = data["id"]

    assert response.status_code == 200
    assert data["id"] == shopping_id
    assert data["name"] == name
    assert data["address"] == address

    new_name = "Colombo 2.0"
    response = client.put(f'/shoppings/{shopping_id}/', params={"shopping_id": shopping_id, "shopping_name": new_name})

    assert response.status_code == 200

    data_response = response.json()

    assert data_response["id"] == shopping_id
    assert data_response["name"] == new_name
    assert data_response["address"] == address

    
# Delete method
def test_delete_shopping():
    name = "Viana Shopping"
    address = "Lisboa"
    response = client.post('/shoppings/', json={"id": 4, "name": name, "address": address})
    
    data = response.json()
    shopping_id = data["id"]

    assert response.status_code == 200
    assert data["id"] == shopping_id
    assert data["name"] == name
    assert data["address"] == address


    response = client.delete(f'/shoppings/{shopping_id}/', params={shopping_id: shopping_id})

    assert response.status_code == 200
    
    response = client.get(f'/shoppings/{shopping_id}/', params={shopping_id: shopping_id})

    assert response.json() == {"detail": "Shopping not found"}

