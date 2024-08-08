import models.indicadores_nutricionales
import schemas.indicadores_nutricionales
from sqlalchemy.orm import Session

def get_indicador_nutricional_by_id(db: Session, id: int):
    return db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.ID == id).first()

def get_indicador_nutricional_by_nombre(db: Session, nombre: str):
    return db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.Nombre == nombre).first()

def get_indicadores_nutricionales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.indicadores_nutricionales.Actividad).offset(skip).limit(limit).all()

def create_indicador_nutricional(db: Session, indicador_nutricional: schemas.indicadores_nutricionales.IndicadorNutricionalCreate):
    db_indicador_nutricional = models.indicadores_nutricionales.Actividad(
        Nombre=indicador_nutricional.Nombre,
        Edad=indicador_nutricional.Edad,
        Genero=indicador_nutricional.Genero,
        Altura=indicador_nutricional.Altura,
        Peso=indicador_nutricional.Peso,
        Imc=indicador_nutricional.Imc,
        Porcentaje_grasa=indicador_nutricional.Porcentaje_grasa,
        Nivel_actividad=indicador_nutricional.Nivel_actividad
    )
    
    db.add(db_indicador_nutricional)
    db.commit()
    db.refresh(db_indicador_nutricional)
    return db_indicador_nutricional

def update_indicador_nutricional(db: Session, id: int, indicador_nutricional: schemas.indicadores_nutricionales.IndicadorNutricionalUpdate):
    db_indicador_nutricional = db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.ID == id).first()
    if db_indicador_nutricional:
        for var, value in vars(indicador_nutricional).items():
            if value is not None:
                setattr(db_indicador_nutricional, var, value)
        db.commit()
        db.refresh(db_indicador_nutricional)
    return db_indicador_nutricional

def delete_indicador_nutricional(db: Session, id: int):
    db_indicador_nutricional = db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.ID == id).first()
    if db_indicador_nutricional:
        db.delete(db_indicador_nutricional)
        db.commit()
    return db_indicador_nutricional

# import models.indicadores_nutricionales
# import schemas.indicadores_nutricionales
# from sqlalchemy.orm import Session

# def get_indicadores_nutricionales(db: Session, id: int):
#     return db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.ID == id).first()

# def get_indicadores_nutricionales_by_id(db: Session, nombre: str):
#     return db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.Nombre == nombre).first()

# def get_indicadores_nutricionales(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.indicadores_nutricionales.Actividad).offset(skip).limit(limit).all()

# def create_indicadores_nutricionales(db: Session, indicadores_nutricionales: schemas.indicadores_nutricionales.IndicadorNutricionalCreate):
#     db_indicadores_nutricionales = models.indicadores_nutricionales.Actividad(
#                                       Nombre=indicadores_nutricionales.Nombre,
#                                       Edad=indicadores_nutricionales.Edad,
#                                       Genero=indicadores_nutricionales.Genero,
#                                       Altura=indicadores_nutricionales.Altura,
#                                       Peso=indicadores_nutricionales.Peso,
#                                       Imc=indicadores_nutricionales.Imc,
#                                       Porcentaje_grasa=indicadores_nutricionales.Porcentaje_grasa,
#                                       Nivel_actividad=indicadores_nutricionales.Nivel_actividad )
    
#     db.add(db_indicadores_nutricionales)
#     db.commit()
#     db.refresh(db_indicadores_nutricionales)
#     return db_indicadores_nutricionales

# def update_indicadores_nutricionales(db: Session, id: int, indicadores_nutricionales: schemas.indicadores_nutricionales.IndicadorNutricionalUpdate):
#     db_indicadores_nutricionales = db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.ID == id).first()
#     if db_indicadores_nutricionales:
#         for var, value in vars(indicadores_nutricionales).items():
#             setattr(db_indicadores_nutricionales, var, value) if value else None
#         db.commit()
#         db.refresh(db_indicadores_nutricionales)
#     return db_indicadores_nutricionales

# def delete_indicadores_nutricionales(db: Session, id: int):
#     db_indicadores_nutricionales = db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.ID == id).first()
#     if db_indicadores_nutricionales:
#         db.delete(db_indicadores_nutricionales)
#         db.commit()
#     return db_indicadores_nutricionales