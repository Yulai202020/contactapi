import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, create_engine, Table, Column, Integer, String

database_url = os.environ.get("DATABASE_URL")

base = declarative_base()
engine = create_engine(database_url)
engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

meta = MetaData()

person = Table(
    "person",
    meta,
    Column("id", Integer, primary_key = True),
    Column("name", String(100), nullable = False),
    Column("surname", String(100), nullable = False),
)

meta.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()