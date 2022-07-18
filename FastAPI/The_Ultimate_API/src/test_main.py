from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_route():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "This is the best API ever made!"}


# Read Tests
def test_read_shopping():
    name = "Braga Parque"
    response = client.get('/shoppings/', json={"id": 1, "name": name})

    data = response.json()

    assert response.status_code == 200
    assert data["name"] == name
    assert data["id"] == 1

# Create Tests
def create_shopping():
    name = "Braga Parque"
    response = client.post('/shoppings/',
                           json={"id": 1, "name": name, "address": "Braga"})

    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["name"] == name
    assert data["address"] == "Braga"

# Update Tests
#def update_shopping_name():
#    response = client.put('/')