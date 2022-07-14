from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:nathanj35@localhost/item_db", echo=True, future=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)