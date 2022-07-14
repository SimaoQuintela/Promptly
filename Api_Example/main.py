from fastapi import Depends, FastAPI, HTTPException,Request, Response
from sqlalchemy.orm import Session

import querys, models, schemas
from database import SessionLocal, engine

from typing import List

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

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/stores/", response_model=schemas.Store)
def create_store(store: schemas.Store, db: Session = Depends(get_db)):
    return querys.create_store(db=db, store=store)

@app.post("/prodtypes/", response_model=schemas.ProductType)
def create_prodType (prodType: schemas.ProductType, db: Session = Depends(get_db)):
    return querys.create_prodType(db=db, prodType=prodType)

@app.post("/store/{store_id}/prodType/{prodType_id}/products/", response_model=schemas.Product)
def create_product (*,product: schemas.Product, db: Session = Depends(get_db),store_id:int,prodType_id:int):
    return querys.create_product(db=db, product=product,store_id=store_id,prodType_id=prodType_id)

@app.get("/stores/", response_model=List[schemas.Store])
def read_users(db: Session = Depends(get_db)):
    users = querys.get_stores(db)
    return users