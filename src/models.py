from config import base
from sqlalchemy import Column, Integer, String


class Person(base):
    __tablename__ = "person"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    surname = Column(String)
