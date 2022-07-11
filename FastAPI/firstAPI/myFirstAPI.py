# First course of FastAPI. 


"""
amazon-com/create-user   -> create-user is an endpoint

GET - Get an information 
POST - Create something new 
PUT - Update something 
DELETE - Delete something

"""

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    }
}
 

class Student(BaseModel):
    name: str
    age: int
    year: str 

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None




@app.get("/")
def index():
    return {"name": "First Data"}

# path parameters
# example of a path parameter: google.com/get-student
#                                       |
#                                  path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None,
                                       description="The ID of the student you want to view",
                                       gt=0,   # the student_id has to be greater than 0
                                       lt=3)):  # the student_id has to be less than 3 
    return students[student_id]


# query parameters
# example of a query parameter: google.com/results?search=Python
#                                                 |
#                                            query parameter
@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"Data": "Not found"}


# query and path parameters combined
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    
    students[student_id] = student
    return students[student_id] 

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]

    return {"Message": "Student deleted successfully"}