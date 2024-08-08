from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date
import enum

class TransaccionesBase(BaseModel):
    Usuario_ID: int
    Metodo_Pago: str
    Numero_Tarjeta : str
    CVC : int 
    Fecha_Expiracion : date
    Monto: float
    Estatus: bool
    Fecha_Registro : datetime
    Fecha_Actualizacion: datetime


class TransaccionCreate(TransaccionesBase):
    pass

class TransaccionUpdate(TransaccionesBase):
    pass

class Transaccion(TransaccionesBase):
    ID: int
    Usuario_ID: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True


