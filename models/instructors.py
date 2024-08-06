from sqlalchemy import Column, Integer, String, Enum, DateTime, Integer
from sqlalchemy.orm import relationship
from config.db import Base
import enum

# Definir los enumeradores si es necesario (ajustar según el caso de uso)
class Gender(str, enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class BloodType(str, enum.Enum):
    AP = "A+"
    AN = "A-"
    BP = "B+"
    BN = "B-"
    ABP = "AB+"
    ABN = "AB-"
    OP = "O+"
    ON = "O-"

class Instructor(Base):
    __tablename__ = "tbb_instructors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80))
    email = Column(String(100), unique=True, index=True)
    specialty = Column(String(100))
    years_of_experience = Column(Integer)
    # Puedes agregar más campos si es necesario

    # Si es necesario, se puede agregar relaciones aquí

    # Otros campos que necesites
