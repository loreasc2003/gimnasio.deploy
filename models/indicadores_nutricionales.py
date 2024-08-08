from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import declarative_base
import enum

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the enum for Gender
class MyGenero(enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"

# Define the enum for Activity Level
class NivelActividad(enum.Enum):
    Sedentario = "Sedentario"
    Ligero = "Ligero"
    Moderado = "Moderado"
    Activo = "Activo"
    Muy_Activo = "Muy Activo"

# Define the model for Actividad
class Actividad(Base):
    __tablename__ = "tbd_indicadores_nutricionales"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(80))
    Edad = Column(Integer)
    Genero = Column(Enum(MyGenero))
    Altura = Column(Float(5, 2))
    Peso = Column(Float(5, 2))
    Imc = Column(Float)
    Porcentaje_grasa = Column(Float)
    Nivel_actividad = Column(Enum(NivelActividad))




# from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum, Float
# from sqlalchemy.dialects.mysql import LONGTEXT
# from sqlalchemy.orm import relationship
# from config.db import Base
# import enum

# class MyGenero(enum.Enum):
#     Masculino = "Masculino"
#     Femenino = "Femenino"

   

# class Actividad(Base):
#     __tablename__ = "tbd_indicadores_nutricionales"

#     ID= Column(Integer, primary_key=True, index=True)
#     Nombre = Column(String(80))
#     Edad = Column(Integer)
#     Genero = Column( Enum(MyGenero))
#     Altura = Column( Float(5,2))
#     Peso = Column( Float(5,2))
#     Imc = Column(Float())
#     Porcentaje_grasa = Column(Float())
#     Nivel_actividad= Column(Enum('Sedentario','Ligero','Moderado','Activo','Muy Activo'))
