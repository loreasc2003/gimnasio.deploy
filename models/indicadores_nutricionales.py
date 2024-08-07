from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Float
from config.db import Base
import enum

class MyGenero(str,enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"

   

class Actividad(Base):
    __tablename__ = "tbb_personas"

    ID= Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(80))
    Edad = Column(Integer(10))
    Genero = Column( Enum(MyGenero))
    Altura = Column( Float(5,2))
    Peso = Column( Float(5,2))
    Imc = Column(Float())
    Porcentaje_grasa = Column(Float())
    Nivel_actividad= Column(Enum('Sedentario','Ligero','Moderado','Activo','Muy Activo'))
