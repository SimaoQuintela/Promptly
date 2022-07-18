from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base

from main import app, get_db

import os

from models import University
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


def test_read_main():
    response = client.get("/")
    #assert response.status_code == 307
    assert response.json() == {"message": "Hello User!"}


def test_create_university():
    response = client.post(
        "/universitys",
        json={"id": "1", "name": "Universidade do Minho"},
    )
    #assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Universidade do Minho"


def test_get_universitys():
    response = client.get(
        "/universitys"
    )
    data = response.json()
    assert data == [{
        "id": 1,
        "name": "Universidade do Minho",
    }]

def test_get_university_students():
    client.post(
        "/courses",
        json = {
            "id": "1",
            "name": "LCC",
            "university": "1",
            }
    )
    resp = client.post(
        "/students",
        json = {
            "id": 1,
            "name": "Pedro",
            "average": 14,
            "university": 1,
            "course": 1
            }
    )
    client.post(
        "/students",
        json = {
            "id": 2,
            "name": "Simão",
            "average": 16,
            "university": 1,
            "course": 1
            }
    )
    data = resp.json()
    uni_id = 1
    response = client.get(f"/all_university_students/{uni_id}/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == [
      {
            "id": 1,
            "name": "Pedro",
            "average": 14,
            "university": 1,
            "course": 1
            },
      {
            "id": 2,
            "name": "Simão",
            "average": 16,
            "university": 1,
            "course": 1
            }
    ]


def test_update_student():
    resp = client.post(
        "/students",
        json={
            "id": 3,
            "name": "Miguel",
            "average": 11,
            "university": 1,
            "course": 1
            },
    )
    data = resp.json()
    stu_id = data["id"]
    response = client.put(
        f"/student/{stu_id}/change",
        params={"id": stu_id,
                "average": 18},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == {
            "id": 3,
            "name": "Miguel",
            "average": 18,
            "university": 1,
            "course": 1
    }
    
    

def test_delete_course():
    resp = client.post(
        "/courses",
        json={
            "id": 2,
            "name": "LEI",
            "university": 1
        },
    )
    data = resp.json()
    course_id = data["id"]
    response = client.delete(f"/course/{course_id}/delete",)
    assert response.status_code == 200, response.text
    assert {
            "id": 2,
            "name": "LEI",
            "university": 1
    }
    
