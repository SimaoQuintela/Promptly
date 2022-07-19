from itertools import product
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    contact = Column(String, index=True, unique=True)
    products = relationship("Product", back_populates="priceStore",cascade="all, delete, delete-orphan")

class Product(Base):
    __tablename__ = "store_products"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer,index=True)
    #aqui é melhor chamar de store_id
    store = Column(Integer, ForeignKey("stores.id"))
    #e aqui de product_id
    product = Column(Integer, ForeignKey("products.id"))
    #e aqui de store
    priceStore = relationship("Store", back_populates="products")
    priceProduct = relationship("ProductType", back_populates="products")
    
#ideal é que o nome da classe seja igual ou muito muito similar ao que esta na base de dados
class ProductType(Base):
    __tablename__ = "products"

    #se nao engano primeray key automaticamente é index tbm
    id = Column(Integer, primary_key=True, index=True)
    #e provavel que unique tbm vira index
    name = Column(String, unique=True, index=True)
    products = relationship("Product", back_populates="priceProduct",cascade="all, delete, delete-orphan")