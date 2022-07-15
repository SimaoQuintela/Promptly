from typing import List

from pydantic import BaseModel

class Course(BaseModel):
    id: int
    name: str
    university: int
    class Config:
        orm_mode = True

class Student(BaseModel):
    id: int
    name: str
    average: int
    university: int
    course: int
    class Config:
        orm_mode = True

class University(BaseModel):
    id:int
    name: str
    class Config:
        orm_mode = True
