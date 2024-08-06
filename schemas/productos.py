from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime


class ProductoBase(BaseModel):
    Nombre: str
    Marca: str
    Cod_barras: str
    Descripcion: str
    Presentacion: str
    Precio_actual: float
    Fotografia: str
    Estatus:bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    ID:int
    class Config:
        orm_mode = True

        