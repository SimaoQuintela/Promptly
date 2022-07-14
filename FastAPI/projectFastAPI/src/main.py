from fastapi import Depends, FastAPI, HTTPException,Request, Response
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

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

@app.get("/stores/", response_model=list[schemas.Store])
def read_stores(db: Session = Depends(get_db)):
    return crud.get_stores(db)

@app.get("/stores/{store_id}", response_model=list[schemas.Store])
def get_store (*,db: Session = Depends(get_db),store_id:int):
    return crud.get_store(db=db,store_id=store_id)

@app.get("/stores/", response_model=list[schemas.Store])
def get_store_byname (*,db: Session = Depends(get_db),store:str):
    return crud.get_store_byname(db=db,name=store)

@app.get("/productTypes/", response_model=list[schemas.ProductType])
def read_prodTypes(db: Session = Depends(get_db)):
    return crud.get_prodTypes(db)

@app.get("/products/", response_model=list[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    return crud.get_products(db)
    