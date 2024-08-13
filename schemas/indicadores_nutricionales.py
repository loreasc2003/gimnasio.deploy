from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date
import enum


class IndicadoresNutricionalesBase(BaseModel):
    Nombre: str
    Edad: int
    Genero: str
    Altura: float
    Peso: float
    Imc: float
    Porcentaje_grasa: float
    NivelActividad: str


class IndicadoresNutricionalesCreate(IndicadoresNutricionalesBase):
    pass

class IndicadoresNutricionalesUpdate(IndicadoresNutricionalesBase):
    pass

class indicador_nutricional(IndicadoresNutricionalesBase):
    ID: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True

