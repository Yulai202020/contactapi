import crud, os
from config import get_db
from schemas import PersonSchema

from sqlalchemy.orm import Session

from fastapi import APIRouter
from fastapi import Depends, APIRouter

table_name: str = os.environ.get("TABLE_NAME")

# Create api router
router = APIRouter()

# Get all Persons
@router.get("/")
async def home_all(db: Session = Depends(get_db)):
    persons = crud.get_person(db = db)
    return persons

# Get person by ID
@router.get("/persons/{person_id}")
async def get_person(person_id: int, db: Session = Depends(get_db)):

    _person = crud.get_person_by_id(db = db, person_id = person_id)
    return _person

# Create Person
@router.get("/create/name={name}/surname={surname}")
async def create_person(name: str, surname: str, db: Session = Depends(get_db)):
    
    _tmp = PersonSchema(name = name, surname = surname)
    _person = crud.create_person(db = db, person = _tmp)

    return {"Massage": "OK"}

# Update person
@router.get("/update/id={person_id}/name={name}/surname={surname}")
async def update_person(person_id: int, name: str, surname: str, db: Session = Depends(get_db)):

    _person = crud.update_person(db = db, name = name, surname = surname)
    return _person

# Delete person
@router.get("/delete/id={person_id}")
async def delete(person_id: int):

    _person = crud.delete_person(person_id = person_id)
    return {"Massage": "OK"}