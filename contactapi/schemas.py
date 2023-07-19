from pydantic import BaseModel, Field
from typing import Optional, TypeVar

T = TypeVar("T")

# Create schemas
class PersonSchema(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None

    class Config:
        orm_mode = True

class RequestPerson(BaseModel):
    parameter: PersonSchema = Field(...)