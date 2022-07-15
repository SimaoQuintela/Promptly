from email.policy import HTTP
from click import help_option
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schemas



# Create methods
def create_shopping(db: Session, shopping: schemas.Shopping):
    new_shopping = models.Shopping( 
        id = shopping.id,
        name = shopping.name,
        address=shopping.address
    )

    db.add(new_shopping)
    db.commit()
    db.refresh(new_shopping)
    return new_shopping

def create_store(db: Session, shopping_id: int, store: schemas.Store):
    shopping = read_shopping(db, shopping_id)

    if shopping.name != store.located_on :
        raise HTTPException(detail="Shopping not found.", status_code= status.HTTP_404_NOT_FOUND)
    
    
    new_store = models.Store(
        id = store.id,
        name = store.name,
        located_on = store.located_on
    )  
    	
    db.add(new_store)
    db.commit()
    db.refresh(new_store)

    return new_store



# Read methods
def read_all_shoppings(db: Session):
    all_shoppings = db.query(models.Shopping).all()

    return all_shoppings

def read_shopping(db: Session, shopping_id: int):
    shopping = db.query(models.Shopping).filter(models.Shopping.id == shopping_id).first()

    if shopping is None:
        raise HTTPException(detail="Shopping not found", status_code=status.HTTP_404_NOT_FOUND)

    return shopping

def read_store(db: Session, store_id: int):
    store = db.query(models.Store).filter(models.Store.id == store_id).first()

    if store is None:
        raise HTTPException(detail="Store not foud", status_code=status.HTTP_404_NOT_FOUND)

    return store


def read_all_stores(db:Session):
    all_stores = db.query(models.Store).all()

    return all_stores