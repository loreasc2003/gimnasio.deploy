import models.membresias
import schemas.membresias
from sqlalchemy.orm import Session
import models, schemas

def get_membresia(db: Session, id: int):
    return db.query(models.membresias.Membresia).filter(models.membresias.Membresia.ID == id).first()

def get_membresia_by_id(db: Session, codigo: str):
    return db.query(models.membresias.Membresia).filter(models.membresias.Membresia.Codigo == codigo).first()

def get_membresias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.membresias.Membresia).offset(skip).limit(limit).all()

def create_membresias(db: Session, nom: schemas.membresias.MembresiaCreate):
    db_user = models.membresias.Membresia(
                                      Codigo=nom.Codigo,
                                      Tipo=nom.Tipo,
                                      Tipo_Servicios=nom.Tipo_Servicios, 
                                      Tipo_Plan=nom.Tipo_Plan,
                                      Nivel=nom.Nivel,  
                                      Fecha_Inicio=nom.Fecha_Inicio,  
                                      Fecha_Fin=nom.Fecha_Fin, 
                                      Estatus=nom.Estatus, 
                                      Fecha_Registro=nom.Fecha_Registro, 
                                      Fecha_Actualizacion=nom.Fecha_Actualizacion )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_membresias(db: Session, id: int, membre: schemas.membresias.MembresiaUpdate):
    db_user = db.query(models.membresias.Membresia).filter(models.membresias.Membresia.ID == id).first()
    if db_user:
        for var, value in vars(membre).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_membresias(db: Session, id: int):
    db_user = db.query(models.membresias.Membresia).filter(models.membresias.Membresia.ID == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user