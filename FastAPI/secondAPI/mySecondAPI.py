# Second course of FastAPI
from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdate

app = FastAPI()

db: List[User] = [
    User(
        id= UUID("8408baac-4960-4a89-be8d-0824baf09f17"),
        first_name= "Jamila",
        last_name= "Ahmed",
        gender= Gender.female,
        roles= [Role.student]
    ),

    User(
        id= UUID("18845873-4a2d-4c3c-b678-893bf736e7e8"),
        first_name= "Alex",
        last_name= "Jones",
        gender= Gender.male,
        roles= [Role.admin, Role.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db  

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)

    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

    raise HTTPException(
        status_code= 404,
        detail =f"User with id: {user_id} does not exists"
    )        

@app.put("/api/v1/users/{user_id}")
def update_user(user_id: UUID, user_update: UserUpdate):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name 

            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name

            if user_update.last_name is not None:
                user.last_name = user_update.last_name 

            if user_update.id is not None:
                user.roles = user_update.roles

    raise HTTPException(
        status_code=404,
        detail = f"User with id {user_id} does not exists"
    )            
