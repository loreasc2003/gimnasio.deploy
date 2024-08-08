from typing import List
from pydantic import BaseModel
import enum

# Define los Enum para coincidir con SQLAlchemy
class MyGenero(str, enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"

class NivelActividad(str, enum.Enum):
    Sedentario = 'Sedentario'
    Ligero = 'Ligero'
    Moderado = 'Moderado'
    Activo = 'Activo'
    Muy_Activo = 'Muy Activo'

class IndicadorNutricionalBase(BaseModel):
    Nombre: str
    Edad: int
    Genero: MyGenero
    Altura: float
    Peso: float
    Imc: float
    Porcentaje_grasa: float
    Nivel_actividad: NivelActividad

class IndicadorNutricionalCreate(IndicadorNutricionalBase):
    pass

class IndicadorNutricionalUpdate(IndicadorNutricionalBase):
    pass

class IndicadorNutricional(IndicadorNutricionalBase):
    ID: int
    # Descomentar y ajustar según el caso
    # owner_id: int  

    class Config:
        from_attributes = True

# from typing import List, Union
# from pydantic import BaseModel
# from datetime import datetime, date
# import enum


# class indicador_nutricionalBase(BaseModel):
#     Nombre: str
#     Edad: int
#     Genero: str
#     Altura: float
#     Peso: float
#     Imc: float
#     Porcentaje_grasa: float
#     Nivel_actividad: enum


# class indicadores_nutricionalesCreate(indicador_nutricionalBase):
#     pass

# class indicadores_nutricionalesUpdate(indicador_nutricionalBase):
#     pass

# class indicadores_nutricionales(indicador_nutricionalBase):
#     ID: int
#     #owner_id: int clave foranea
#     class Config:
#         orm_mode = True

