import models.indicadores_nutricionales
import schemas.indicadores_nutricionales
from sqlalchemy.orm import Session

def get_indicador_nutricional(db: Session, id: int):
    return db.query(models.indicadores_nutricionales.IndicadoresNutricionales).filter(models.indicadores_nutricionales.IndicadoresNutricionales.ID == id).first()

def get_indicadores_nutricionales_by_id(db: Session, nombre: str):
    return db.query(models.indicadores_nutricionales.IndicadoresNutricionales).filter(models.indicadores_nutricionales.IndicadoresNutricionales.Nombre == nombre).first()

def get_indicadores_nutricionales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.indicadores_nutricionales.IndicadoresNutricionales).offset(skip).limit(limit).all()
def create_indicadores_nutricionales(db: Session, indicadores_nutricionales: schemas.indicadores_nutricionales.IndicadoresNutricionalesCreate):
    db_indicadores_nutricionales = models.indicadores_nutricionales.IndicadoresNutricionales(
                                      Nombre=indicadores_nutricionales.Nombre,
                                      Edad=indicadores_nutricionales.Edad,
                                      Genero=indicadores_nutricionales.Genero,
                                      Altura=indicadores_nutricionales.Altura,
                                      Peso=indicadores_nutricionales.Peso,
                                      Imc=indicadores_nutricionales.Imc,
                                      Porcentaje_grasa=indicadores_nutricionales.Porcentaje_grasa,
                                      NivelActividad=indicadores_nutricionales.NivelActividad )
    
    db.add(db_indicadores_nutricionales)
    db.commit()
    db.refresh(db_indicadores_nutricionales)
    return db_indicadores_nutricionales

def update_indicadores_nutricionales(db: Session, id: int, indicadores_nutricionales: schemas.indicadores_nutricionales.IndicadoresNutricionalesUpdate):
    db_indicadores_nutricionales = db.query(models.indicadores_nutricionales.IndicadoresNutricionales).filter(models.indicadores_nutricionales.IndicadoresNutricionales.ID == id).first()
    if db_indicadores_nutricionales:
        for var, value in vars(indicadores_nutricionales).items():
            setattr(db_indicadores_nutricionales, var, value) if value else None
        db.commit()
        db.refresh(db_indicadores_nutricionales)
    return db_indicadores_nutricionales

def delete_indicadores_nutricionales(db: Session, id: int):
    db_indicadores_nutricionales = db.query(models.indicadores_nutricionales.IndicadoresNutricionales).filter(models.indicadores_nutricionales.IndicadoresNutricionales.ID == id).first()
    if db_indicadores_nutricionales:
        db.delete(db_indicadores_nutricionales)
        db.commit()
    return db_indicadores_nutricionales