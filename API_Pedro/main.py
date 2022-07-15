from urllib import response
from fastapi import Depends, FastAPI, HTTPException,Request, Response
from sqlalchemy.orm import Session

import querys, models, schema
from database import SessionLocal, engine

from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"message": "Hello User!"}


@app.get('/universitys', response_model= List[schema.University])
def get_universitys(db: Session = Depends(get_db)):
    return querys.get_universitys(db)

@app.get('/all_university_students/{university_id}/', response_model= List[schema.Student])
def get_all_university_students(university_id:int, db: Session = Depends(get_db)):
    return querys.get_all_university_students(db=db, uni_id=university_id)

@app.get('/students', response_model= List[schema.Student])
def get_students(db: Session = Depends(get_db)):
    return querys.get_studentes(db)

@app.get('/courses', response_model= List[schema.Course])
def get_courses(db: Session = Depends(get_db)):
    return querys.get_courses(db)

@app.post('/universitys', response_model=schema.University)
def create_university(university: schema.University, db: Session = Depends(get_db)):            
    return querys.create_university(db=db, uni=university) 

@app.post('/students', response_model=schema.Student)
def create_student(student: schema.Student, db: Session = Depends(get_db)):        
    return querys.create_student(db, student) 

@app.post('/courses', response_model=schema.Course)
def create_course(course: schema.Course, db: Session = Depends(get_db)):
    return querys.create_course(db=db, cur=course) 


@app.put("/student/{student_id}/change", response_model=schema.Student)
def change_student_average (student_id:int, average:int, db: Session = Depends(get_db)):
    return querys.change_student_average(db=db,student_id=student_id,new_average=average)


@app.delete("/university/{university_id}/delete", response_model=schema.University)
def delete_university (university_id:int, db: Session = Depends(get_db)):
    return querys.remove_university(db,university_id)

@app.delete("/student/{student_id}/delete", response_model=schema.University)
def delete_student (student_id:int, db: Session = Depends(get_db)):
    return querys.remove_student(db,student_id)

@app.delete("/course/{course_id}/delete", response_model=schema.Course)
def delete_course (course_id:int, db: Session = Depends(get_db)):
    return querys.remove_course(db,course_id)