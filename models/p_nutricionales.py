from sqlalchemy import Column, Boolean, Integer, String, DateTime, Enum
from config.db import Base
import enum

# Define el Enum para TipoRespuesta
class TipoRespuesta(enum.Enum):
    Abierta = "Abierta"
    Cerrada = "Cerrada"

# Define el modelo de SQLAlchemy
class p_nutricionales(Base):
    __tablename__ = 'tbb_preguntas_nutricionales'

    ID = Column(Integer, primary_key=True, index=True)
    Pregunta = Column(String(255))  
    Tipo_Respuesta = Column(Enum(TipoRespuesta))
    Descripcion = Column(String(255))  
    Fecha_Creacion = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Estatus = Column(Boolean, default=False)
    Opciones_Respuesta = Column(String(255))  
