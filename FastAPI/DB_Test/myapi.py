from code import interact
from email.header import Header
from http.client import HTTPResponse
from operator import gt
from urllib import request, response
from fastapi import FastAPI, Path, Depends
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models
from models import Alunos

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.on_event("startup")
def startup_populate_db():
    db = SessionLocal()
    num_alunos = db.query(models.Alunos).count()
    
    if num_alunos == 0:
        alunos = [
            {
                "nome": "Afonso Aaaarão",
                "idade": 21,
                "turma": "Desistiu"
            },
            {
                "nome": "Eduardo Sant'Anna",
                "idade": 20,
                "turma": "Rap"
            },
            {
                "nome": "Pedro Fernandes",
                "idade": 20,
                "turma": "LCC"
            },
            {
                "nome": "Francisco Teófilo",
                "idade": 21,
                "turma": "MAximinense"
            },
            {
                "nome": "Bruno Jardim",
                "idade": 20,
                "turma": "LCC"
            },
            {
                "nome": "Maria Martins",
                "idade": 20,
                "turma": "Química"
            }
        ]
        
        for aluno in alunos:
            db.add(models.Alunos(**aluno))
        db.commit()
    else:
        print(f"{num_alunos} alunos na base de dados")
    db.close()
    



def lista_Alunos(
    #request: Request,
    hx_request: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    db_alunos = db.query(models.Alunos).all()
    print(db_alunos)












'''
O formato dos alunos era este, mas para trabalhar com db, dava mais jeito tirar os id's, então pronto


alunos = {
        1: {
            "nome": "Afonso Aaaarão",
            "idade": 21,
            "turma": "Desistiu"
        },
        2: {
            "nome": "Eduardo Sant'Anna",
            "idade": 20,
            "turma": "Rap"
        },
        3: {
            "nome": "Pedro Fernandes",
            "idade": 20,
            "turma": "LCC"
        },
        4: {
            "nome": "Francisco Teófilo",
            "idade": 21,
            "turma": "MAximinense"
        },
        5: {
            "nome": "Bruno Jardim",
            "idade": 20,
            "turma": "LCC"
        },
        6: {
            "nome": "Maria Martins",
            "idade": 20,
            "turma": "Química"
        }
    }
'''

class Aluno(BaseModel):
    nome: str
    idade: int
    turma: str

class UpdateAluno(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    turma: Optional[str] = None



@app.get("/get-aluno/{id_aluno}")
def get_aluno(id: int):
    return alunos[id]

@app.get("/get-by-name")
def get_aluno(nome : Optional[str] = Path(None, description = "Nome do Aluno que queremos ver")):
    for aluno in alunos:
        if alunos[aluno]["nome"] == nome:
            return alunos[aluno]
    return {"Data": "Not Found"}

@app.post("/create-aluno/{id}")
def create_aluno(id: int, aluno: Aluno):
    if id in alunos:
        return{"Error": "Student Exists"}
    else:
        alunos[id] = aluno
        return alunos[id]

@app.put("/update-aluno/{id}")
def update_aluno(id: int, aluno: UpdateAluno):
    if id  not in alunos:
        return {"Error": "Not Found"}
    alunos[id] = aluno
    return alunos[id]

@app.delete("/delete-aluno/{id}")
def delete_aluno(id: int):
    if id  not in alunos:
        return {"Error": "Not Found"}
    del alunos[id]
    return {"Message": "Aluno eliminado com sucesso!"}