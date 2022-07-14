from itertools import product
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    price: int
    store: int
    product: int
    class Config:
        orm_mode = True


class ProductType(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True
    

class Store(BaseModel):
    id: int
    name: str
    address: str
    class Config:
        orm_mode = True
    