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
    store = Column(Integer, ForeignKey("stores.id"))
    product = Column(Integer, ForeignKey("products.id"))
    priceStore = relationship("Store", back_populates="products")
    priceProduct = relationship("ProductType", back_populates="products")
    

class ProductType(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    products = relationship("Product", back_populates="priceProduct",cascade="all, delete, delete-orphan")