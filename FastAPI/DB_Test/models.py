from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Alunos(Base):
    __tablename__ = "Alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    idade = Column(Integer)
    turma = Column(String)


'''
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