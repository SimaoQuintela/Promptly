from typing import Union
from pydantic import BaseModel


class Shopping(BaseModel):
    id: int
    name: str
    address: Union[str, None] = None

    class Config:
        orm_mode = True



class Store(BaseModel):
    id: int
    name: Union[str, None] = None 
    located_on: str

    class Config:
        orm_mode = True


class Employee(BaseModel):
    id: int
    name: Union[str, None] = None
    working_on: str

    class Config:
        orm_mode = True