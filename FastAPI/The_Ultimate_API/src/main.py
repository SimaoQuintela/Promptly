from ast import List
from fastapi import Depends, FastAPI, Request, Response
from matplotlib.pyplot import get
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)

    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()

    return response        

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 

@app.get('/')
def route():
    return {"message": "This is the best API ever made!"}


# Read methods
@app.get('/shoppings/', response_model = list[schemas.Shopping])
def read_all_shoppings(db: Session = Depends(get_db)):
    return crud.read_all_shoppings(db=db)

@app.get('/stores/', response_model=list[schemas.Store])
def read_all_stores(db: Session = Depends(get_db)):
    return crud.read_all_stores(db=db)

@app.get('/employees/', response_model=list[schemas.Employee])
def read_all_employees(db: Session = Depends(get_db)):
    return crud.read_all_employees(db=db)


@app.get('/shoppings/{shopping_id}/', response_model=schemas.Shopping)
def read_shopping(shopping_id: int, db: Session = Depends(get_db)):
    return crud.read_shopping(db=db, shopping_id=shopping_id)

@app.get('/shopping/{shopping_id}/stores/', response_model=list[schemas.Store])
def read_shopping_stores(shopping_id: int, db: Session = Depends(get_db)):
    return crud.read_shopping_stores(db=db, shopping_id=shopping_id)

@app.get('/stores/{store_id}/', response_model=schemas.Store)
def read_store(store_id: int, db: Session = Depends(get_db)):
    return crud.read_store(db=db, store_id=store_id)


# Create methods
@app.post('/shoppings/', response_model=schemas.Shopping)
def create_shopping(shopping: schemas.Shopping, db: Session = Depends(get_db)):
    return crud.create_shopping(db=db, shopping=shopping)

@app.post('/shoppings/{shopping_id}', response_model=schemas.Store)
def create_store(shopping_id: int, store: schemas.Store, db: Session = Depends(get_db)):

    return crud.create_store(db=db, shopping_id=shopping_id, store=store)

@app.post('/shoppings/stores/{store_id}/', response_model=schemas.Employee)
def create_employee(store_id: int, employee: schemas.Employee, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, store_id=store_id, employee=employee)


# Update methods
@app.put('/shopping/{shopping_id}/', response_model=schemas.Shopping)
def update_shopping_name(shopping_id: int, shopping_name: str, db: Session = Depends(get_db)):
    return crud.update_shopping_name(db=db, shopping_id=shopping_id, shopping_name=shopping_name)


# Delete methods
@app.delete('/shopping/{shopping_id}/', response_model=schemas.Shopping)
def delete_shopping(shopping_id: int, db: Session = Depends(get_db)):
    return crud.delete_shopping(db=db, shopping_id=shopping_id)