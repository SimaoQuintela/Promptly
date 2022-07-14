from typing import Union
from pydantic import BaseModel

class ProductBase(BaseModel):
    price:int

class Product(ProductBase):
    id:int
    store: int
    product: int
    class Config:
        orm_mode = True


class ProductTypeBase(BaseModel):
    name: str
    

class ProductType(ProductTypeBase):
    id: int
    products: list[Product]= []
    class Config:
        orm_mode = True

class StoreBase(BaseModel):
    name: str
    address: Union[str,None]=None

class Store(StoreBase):
    id: int
    products: list[Product]= []
    class Config:
        orm_mode = True