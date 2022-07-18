from typing import Union
from pydantic import BaseModel


class Shopping(BaseModel):
    id: int
    name: str
    address: str

    class Config:
        orm_mode = True



class Store(BaseModel):
    id: int
    name: Union[str, None] = None
    located_on: int

    class Config:
        orm_mode = True


class Employee(BaseModel):
    id: int
    name: Union[str, None] = None
    working_on: int

    class Config:
        orm_mode = True