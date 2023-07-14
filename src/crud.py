from models import Person
from schemas import PersonSchema
from sqlalchemy.orm import Session

# Get all person
def get_person(db: Session):
    return db.query(Person).all()

# Get person by id
def get_person_by_id(db: Session, person_id: int):
    return db.query(Person).filter(Person.id == person_id).first()

# Create Person
def create_person(db: Session, person: PersonSchema):
    _person = Person(name = person.name, surname = person.surname)
    db.add(_person)
    db.commit()
    db.refresh(_person)
    return _person

# Delete person
def delete_person(db: Session, person_id: int):
    _person = get_person_by_id(person_id)
    db.delete(_person)
    db.commit()

# Update Person
def update_person(db: Session, person_id: int, name: str, surname: str):
    _person = get_person_by_id(db = db, person_id = person_id)
    _person.name = name
    _person.surname = surname
    db.commit()
    db.refresh(_person)
    return _person