from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship  # Asegúrate de importar relationship
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'tbb_usuarios'
    
    ID = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    # Otros campos que puedan estar en la tabla `tbb_usuarios`

class Persona(Base):
    __tablename__ = 'tbb_personas'
    
    ID = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    # Otros campos que puedan estar en la tabla `tbb_personas`

class OpinionCliente(Base):
    __tablename__ = 'tbd_opinion_cliente'
    
    id = Column(Integer, primary_key=True, index=True)
    Usuario_ID = Column(Integer, ForeignKey("tbb_usuarios.ID"))
    descripcion = Column(LONGTEXT, nullable=False)
    tipo = Column(String(100))
    respuesta = Column(LONGTEXT)
    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, onupdate=datetime.utcnow)
    Persona_Id = Column(Integer, ForeignKey("tbb_personas.ID"))

    # Relaciones opcionales para facilitar el acceso a los datos relacionados
    usuario = relationship("Usuario")
    persona = relationship("Persona")
