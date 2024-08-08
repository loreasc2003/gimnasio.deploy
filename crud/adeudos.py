import models.adeudos
import schemas.adeudos
from sqlalchemy.orm import Session

def get_adeudo(db:Session, ID:int):
    return db.query(models.adeudos.adeudos).filter(models.adeudos.adeudos.ID == ID).first()

def get_adeudo_by_nombre(db: Session, nombre: str):
    return db.query(models.adeudos.adeudos).filter(models.adeudos.adeudos == nombre).first()

def get_adeudos(db: Session, skip:int=0,limit:int=10):
    return db.query(models.adeudos.adeudos).offset(skip).limit(limit).all()

def create_adeudos(db: Session, adeudos:schemas.adeudos.AdeudoCreate):
    db_adeudo = models.adeudos.Adeudo(area=adeudos.area, cliente=adeudos.cliente, fecha_registro=person.Fecha_Registro, fecha_actualizacion=person.fecha_actualizacion, estatus=adeudos.estatus, tipo=adeudos.tipo, detalle=adeudos.detalle)
    db.add(db_adeudo)
    db.commit()
    db.refresh(db_adeudo)
    return db_adeudo

def update_adeudo(db: Session, ID: int, adeudos: schemas.adeudos.AdeudoUpdate):
    db_adeudo = db.query(models.adeudos.Adeudo).filter(models.adeudos.Adeudo.ID == ID).first()
    if db_adeudo:
        for var, value in vars(adeudos).items():
            setattr(db_adeudo, var, value) if value else None
        db.commit()
        db.refresh(db_adeudo)
    return db_adeudo

def delete_adeudo(db: Session, ID: int):
    db_adeudo = db.query(models.adeudos.Adeudo).filter(models.adeudos.Adeudo.ID == ID).first()
    if  db_adeudo:
        db.delete(db_adeudo)
        db.commit()
    return db_adeudo

