from pydantic import BaseModel

class Product(BaseModel):
    price:int
    class Config:
        orm_mode = True



class ProductType(BaseModel):
    name: str
    products: list[Product]= []
    class Config:
        orm_mode = True

class Store(BaseModel):
    name: str
    address: str
    products: list[Product]= []
    class Config:
        orm_mode = True