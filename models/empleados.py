from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class Empleado(Base):
    __tablename__ = "tbb_empleados"
    
    ID = Column(Integer, primary_key=True, index=True)
    Area_ID = Column(Integer)
    Fecha_Contratacion = Column(DateTime)
    Puesto_ID = Column(Integer)
    Persona_ID = Column(Integer)
    Numero_Empleado = Column(String(45))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Estatus = Column(Boolean, default=False)
