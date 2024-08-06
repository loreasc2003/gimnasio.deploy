from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

# Base class for Instructor schemas
class InstructorBase(BaseModel):
    name: str
    email: str
    specialty: str
    years_of_experience: int

class InstructorCreate(InstructorBase):
    pass

class InstructorUpdate(InstructorBase):
    pass

class Instructor(InstructorBase):
    id: int
    class Config:
        orm_mode = True
