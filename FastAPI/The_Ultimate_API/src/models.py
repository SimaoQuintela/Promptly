
from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Shopping(Base):
    __tablename__ = "shoppings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String, index=True)

    def __repr__(self):
        return f"<Shopping id: {self.id} name: {self.name} address: {self.address}"

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    located_on = Column(String, ForeignKey("shoppings.name"))

    def __repr__(self):
        return f"<Store id: {self.id} name: {self.name} located_on: {self.located_on}"

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    working_on = Column(String, ForeignKey("stores.name"))

    def __repr__(self):
        return f"<Employee id: {self.id} name: {self.name} working_on: {self.address}"
