from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    university = Column(Integer, ForeignKey("university.id"))
    #cautela com mistura de linguagens
    alunos = relationship("Student", back_populates="curso")

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)
    average = Column(Integer,index = True)
    university = Column(Integer, ForeignKey("university.id"))
    course = Column(Integer, ForeignKey("course.id"))

    curso = relationship("Course", back_populates="alunos")
    uni = relationship("University", back_populates="alun")


class University(Base):
    __tablename__ = "university"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    alun = relationship("Student", back_populates="uni")
    
