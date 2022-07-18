from http.client import HTTP_PORT
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

def create_store(db: Session, store: schemas.Store):
    
    new_store = models.Store(
        id = store.id,
        name = store.name,
        located_on = store.located_on
    )  
    	
    db.add(new_store)
    db.commit()
    db.refresh(new_store)

    return new_store

def create_employee(db: Session, employee: schemas.Employee):
    
    new_employee = models.Employee(
        id = employee.id,
        name = employee.name,
        working_on = employee.working_on
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee





# Read methods
# Missing: Read by shopping, Read by Store
def read_all_shoppings(db: Session):
    all_shoppings = db.query(models.Shopping).all()

    return all_shoppings

def read_shopping(db: Session, shopping_id: int):
    shopping = db.query(models.Shopping).filter(models.Shopping.id == shopping_id).first()

    if shopping is None:
        raise HTTPException(detail="Shopping not found", status_code=status.HTTP_404_NOT_FOUND)

    return shopping

def read_shopping_stores(db: Session, shopping_id: int):
    shopping_name = read_shopping(db=db, shopping_id=shopping_id).name
    print(shopping_name)

    shopping_stores = db.query(models.Store).filter(models.Store.located_on == shopping_name).all()

    return shopping_stores

def read_store(db: Session, store_id: int):
    store = db.query(models.Store).filter(models.Store.id == store_id).first()

    if store is None:
        raise HTTPException(detail="Store not foud", status_code=status.HTTP_404_NOT_FOUND)

    return store


def read_all_stores(db:Session):
    all_stores = db.query(models.Store).all()

    return all_stores


def read_all_employees(db: Session):
    all_employees = db.query(models.Employee).all()

    return all_employees


# Update methods
def update_shopping_name(db: Session, shopping_id: int, shopping_name: str):
    shopping_update = read_shopping(db=db, shopping_id=shopping_id)

    if shopping_update:
        shopping_update.name = shopping_name
        db.commit()

    return shopping_update


# Delete methods
def delete_shopping(db: Session, shopping_id: int):
    shopping_to_delete = read_shopping(db=db, shopping_id=shopping_id)

    if shopping_to_delete:
        db.delete(shopping_to_delete)
        db.commit()
    else:
        raise HTTPException(detail="Shopping not found", status_code=status.HTTP_404_NOT_FOUND)    

    return shopping_to_delete
