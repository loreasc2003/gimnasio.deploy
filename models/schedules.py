from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class Schedule(Base):
    __tablename__ = 'tbb_horarios'
    ID = Column(Integer, primary_key=True, index=True)
    Usuario = Column(String(60))
    Tipo = Column(String(80))
    Fecha_Inicio = Column(DateTime)
    Fecha_Fin = Column(DateTime)
    Fecha_Registro = Column(DateTime)
    Estatus = Column(Boolean, default=False)
    Empleado_ID= Column(Integer, ForeignKey("tbb_empleados.ID"))
    Sucursal_ID = Column(Integer, ForeignKey("tbc_sucursales.Id"))
    Servicio_ID = Column(Integer, ForeignKey("tbc_servicios_clientes.ID"))

    # Id_persona = Column(Integer)
    # intems = relationship("Item", back_populates="owner") Clave foranea