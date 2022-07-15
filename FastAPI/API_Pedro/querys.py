from sqlite3 import IntegrityError
from sqlalchemy.orm import Session

import models, schema

def get_university(db: Session, uni_id: int):
    return db.query(models.University).filter(models.University.id == uni_id).first()

def get_universitys(db: Session):
    return db.query(models.University).all()

def get_student(db: Session, stu_id: int):
    return db.query(models.Student).filter(models.Student.id == stu_id).first()

def get_studentes(db: Session):
    return db.query(models.Student).all()

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_courses(db: Session):
    return db.query(models.Course).all()

def get_all_university_students(db: Session, uni_id: int):
    return db.query(models.Student).filter(models.Student.university == uni_id).all()


def create_university(db: Session, uni: schema.University):
    db_university = models.University(id=uni.id, name=uni.name)
    db.add(db_university)
    db.commit()
    db.refresh(db_university)
    
    return db_university

def create_course(db: Session, cur: schema.Course):
    db_course = models.Course(id=cur.id, name=cur.name, university=cur.university)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    
    return db_course

def create_student(db: Session, stu: schema.Student):
    db_student = models.Student(id=stu.id, name=stu.name, average=stu.average, university=stu.university, course=stu.course)    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def change_student_average(db:Session, student_id:int, new_average:int):
    student = get_student(db=db,stu_id=student_id)
    if (student):
        student.average = new_average
    db.commit()
    return student


def remove_university(db:Session, uni_id:int):
    university = get_university(db=db,uni_id=uni_id)
    if (university):
        db.delete(university)
        db.commit()
    return university

def remove_student(db:Session, stu_id:int):
    student = get_student(db=db, stu_id=stu_id)
    if (student):
        db.delete(student)
        db.commit()
    return student

def remove_course(db:Session, course_id:int):
    course = get_course(db=db, course_id=course_id)
    if (course):
        db.delete(course)
        db.commit()
    return course