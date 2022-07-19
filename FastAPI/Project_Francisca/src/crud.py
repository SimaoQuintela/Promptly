from sqlalchemy.orm import Session

from . import models, schemas

#estas tres funcoes abaixo por estarem num projeto de estudo é ok estarem no mesmo ficheiro
#mas ao fazer projetos é importante separar os ficheiros por dominios ou subdominios
#o store e product podem estar cada um em seu ficheiro
def create_store(db: Session, store: schemas.StoreBase):
    db_store = models.Store(name=store.name,address=store.address)
    db.add(db_store)
    # fazer tratamento de erros, aqui a base de dados pode lancar excecao
    db.commit()
    db.refresh(db_store)
    return db_store

def create_prodType(db: Session, prodType: schemas.ProductTypeBase):
    db_prodType = models.ProductType(name=prodType.name)
    db.add(db_prodType)
    #fazer tratamento de erros, aqui a base de dados pode lancar excecao
    db.commit()
    db.refresh(db_prodType)
    return db_prodType

def create_product (db: Session, product: schemas.ProductBase, store_id: int,prodType_id: int):
    db_product = models.Product(price=product.price, store=store_id,product=prodType_id)
    db.add(db_product)
    # fazer tratamento de erros, aqui a base de dados pode lancar excecao
    db.commit()
    db.refresh(db_product)
    return db_product


def get_store(db: Session, store_id: int):
    #esse first pode lancar excecao, talvez melhor usar o one_or_none
    return db.query(models.Store).filter(models.Store.id == store_id).first()

#melhor user get_store_by_name
def get_store_byname(db: Session, name: str):
    # esse first pode lancar excecao
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
    #o else pode subir um erro do crud pro main e o main lancar um erro do tipo 400 (bad request)
    #pois foi pedido a mudanca de um nome de um store que nao existe
    db.commit()
    return store

def change_product_price(db:Session,store_id:int,productType_id:int,new_price:int):
    product = get_product(db=db,store_id=store_id,prodType_id=productType_id)
    if (product):
        product.price = new_price
        db.commit()
    #vide comentario da linha 72
    return product

def remove_store(db:Session, store_id:int):
    store = get_store(db=db,store_id=store_id)
    if (store):
        db.delete(store)
        db.commit()
    # vide comentario da linha 72
    return store

    
