from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Float
from config.db import Base
import enum

class MyGenero(str,enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"

class MyNivelActividad(str,enum.Enum):
    Sedentario= "Sedentario"
    Ligero= "Ligero"
    Moderado= "Moderado"
    Activo= "Activo"
    MuyActivo= "Muy Activo"

   

class IndicadoresNutricionales(Base):
    __tablename__ = "tbb_indicadores_nutricionales"

    ID= Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(80))
    Edad = Column(Integer)
    Genero = Column( Enum(MyGenero))
    Altura = Column( Float(5,2))
    Peso = Column( Float(5,2))
    Imc = Column(Float())
    Porcentaje_grasa = Column(Float())
    NivelActividad= Column(Enum(MyNivelActividad))
