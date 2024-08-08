from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date
import enum


class indicador_nutricionalBase(BaseModel):
    Nombre: str
    Edad: int
    Genero: str
    Altura: float
    Peso: float
    Imc: float
    Porcentaje_grasa: float
    Nivel_actividad: enum


class indicadores_nutricionalesCreate(indicador_nutricionalBase):
    pass

class indicadores_nutricionalesUpdate(indicador_nutricionalBase):
    pass

class indicadores_nutricionales(indicador_nutricionalBase):
    ID: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True

