from typing import Union
from pydantic import BaseModel

#considere tambem que schemas da mesma entidade podem ser
#diferentes pra ocasioes diferentes, por exemplo: fazer um create de um produto
#nao deve exigir um id, mas para fazer um update sim. vale ressaltar tambem
#que o ideal é que se a propriedade tem nome sem sufixo "id" entao deveria ser a
#entidade em si e nao o id dela.
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
    contact: Union[str,None]=None

class Store(StoreBase):
    id: int
    products: list[Product]= []
    class Config:
        orm_mode = True