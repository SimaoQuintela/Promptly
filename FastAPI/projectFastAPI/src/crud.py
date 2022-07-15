from sqlalchemy.orm import Session

from . import models, schemas

def create_store(db: Session, store: schemas.StoreBase):
    db_store = models.Store(name=store.name,address=store.address)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

def create_prodType(db: Session, prodType: schemas.ProductTypeBase):
    db_prodType = models.ProductType(name=prodType.name)
    db.add(db_prodType)
    db.commit()
    db.refresh(db_prodType)
    return db_prodType

def create_product (db: Session, product: schemas.ProductBase, store_id: int,prodType_id: int):
    db_product = models.Product(price=product.price, store=store_id,product=prodType_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



def get_store(db: Session, store_id: int):
    return db.query(models.Store).filter(models.Store.id == store_id).first()

def get_store_byname(db: Session, name: str):
    return db.query(models.Store).filter(models.Store.name == name).first()

def get_stores(db: Session):
    return db.query(models.Store).all()




def get_prodType(db: Session, prodType_id: int):
    return db.query(models.ProductType).filter(models.ProductType.id == prodType_id).first()

def get_prodType_byname(db: Session, name: str):
    return db.query(models.ProductType).filter(models.ProductType.name == name).first()

def get_prodTypes(db: Session):
    return db.query(models.ProductType).all()



def get_store_products (db: Session, store_id: int):
    return db.query(models.Product).filter(models.Product.store == store_id).all()

def get_product(db: Session, store_id: int,prodType_id: int):
    return db.query(models.Product).filter(models.Store.id == store_id).filter(models.ProductType.id == prodType_id).first()

def get_products (db: Session):
    return db.query(models.Product).all()

def change_store_name(db:Session, store_id:int, new_name:str):
    store = get_store(db=db,store_id=store_id)
    if (store):
        store.name = new_name
    db.commit()
    return store

def change_product_price(db:Session,store_id:int,productType_id:int,new_price:int):
    product = get_product(db=db,store_id=store_id,prodType_id=productType_id)
    if (product):
        product.price = new_price
        db.commit()
    return product

def remove_store(db:Session, store_id:int):
    store = get_store(db=db,store_id=store_id)
    if (store):
        db.delete(store)
        db.commit()
    return store
