from urllib import response
<<<<<<< HEAD

=======
from xxlimited import new
>>>>>>> 117352fb73a93c05101b824a4b0604fba06318c2
from fastapi import Depends, FastAPI, HTTPException,Request, Response
from sqlalchemy.orm import Session

import crud, models, schemas
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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/stores/", response_model=schemas.Store)
def create_store(store: schemas.StoreBase, db: Session = Depends(get_db)):
    return crud.create_store(db=db, store=store)

@app.post("/prodtypes/", response_model=schemas.ProductType)
def create_prodType (prodType: schemas.ProductTypeBase, db: Session = Depends(get_db)):
    return crud.create_prodType(db=db, prodType=prodType)

@app.post("/store/{store_id}/prodType/{prodType_id}/products/", response_model=schemas.Product)
def create_product (*,product: schemas.ProductBase, db: Session = Depends(get_db),store_id:int,prodType_id:int):
    return crud.create_product(db=db, product=product,store_id=store_id,prodType_id=prodType_id)


@app.get("/store/{store_id}", response_model=schemas.Store)
def get_store (store_id:int,db: Session = Depends(get_db)):
    return crud.get_store(db=db,store_id=store_id)

@app.get("/store/", response_model=schemas.Store)
def get_store_byname (store:str,db: Session = Depends(get_db)):
    return crud.get_store_byname(db=db,name=store)

@app.get("/stores/", response_model=List[schemas.Store])
def read_stores(db: Session = Depends(get_db)):
    return crud.get_stores(db)


@app.get("/productType/{prodType_id}", response_model=schemas.ProductType)
def get_prodType (prodType_id:int,db: Session = Depends(get_db)):
    return crud.get_prodType(db=db,prodType_id=prodType_id)

@app.get("/productType/", response_model=schemas.ProductType)
def get_prodType_byname (prodType:str,db: Session = Depends(get_db)):
    return crud.get_prodType_byname(db=db,name=prodType)

@app.get("/productTypes/", response_model=List[schemas.ProductType])
def read_prodTypes(db: Session = Depends(get_db)):
    return crud.get_prodTypes(db)

@app.get("/productType/{prodType_id}/store/{store_id}", response_model=schemas.Product)
def get_product (prodType_id:int,store_id:int,db: Session = Depends(get_db)):
    return crud.get_product(db=db,store_id=store_id,prodType_id=prodType_id)

@app.get("/products/{store_id}", response_model=List[schemas.Product])
def get_store_products (store_id:int,db: Session = Depends(get_db)):
    return crud.get_store_products(db=db,store_id=store_id)

@app.get("/products/", response_model=List[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@app.put("/store/{store_id}/change", response_model=schemas.Store)
def change_store_name (store_id:int, name:str, db: Session = Depends(get_db)):
    return crud.change_store_name(db=db,store_id=store_id,new_name=name)

@app.put("/productType/{prodType_id}/store/{store_id}/change/{price}", response_model=schemas.Product)
def change_product_price (store_id:int, prodType_id:int, price:int, db: Session = Depends(get_db)):
    return crud.change_product_price(db=db,store_id=store_id,productType_id=prodType_id,new_price=price)

@app.delete("/store/{store_id}/delete", response_model=schemas.Store)
def delete_store (store_id:int, db: Session = Depends(get_db)):
<<<<<<< HEAD
    return crud.remove_store(db=db,store_id=store_id)
=======
    return crud.remove_store(db=db,store_id=store_id)
>>>>>>> 117352fb73a93c05101b824a4b0604fba06318c2
