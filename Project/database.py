from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:nathanj35@localhost/")