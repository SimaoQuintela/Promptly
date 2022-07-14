from itertools import product
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    price: int
    store: int
    product: int


class ProductType(BaseModel):
    id: int
    name: str
    

class Store(BaseModel):
    id: int
    name: str
    address: str
    