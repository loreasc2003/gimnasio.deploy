from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from Config.db import Base
import enum

class MyDetalle(enum.Enum):
    Producto ="Masculino"
    Equipamiento ="Femenino"
    Servicio = "Servicio"


class adeudos(Base):
    __tablename__ = "tbd_aduedos"
    
    ID = Column(Integer, primary_key=True, index=True)
    Area = Column(String(255))
    Cliente = Column(String(255))
    Descripcion = Column(String(255))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Estatus = Column(Boolean, default=False)
    Tipo = Column(String(255))
    Detalle = Column(Enum(MyDetalle))  
    