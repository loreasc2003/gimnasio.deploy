import models.promociones
import schemas.promociones
from sqlalchemy.orm import Session

# Buscar una promoción por ID
def get_promocion(db: Session, id: int):
    return db.query(models.promociones.Promocion).filter(models.promociones.Promocion.ID == id).first()

# Buscar una promoción por tipo
def get_promocion_by_tipo(db: Session, tipo: str):
    return db.query(models.promociones.Promocion).filter(models.promociones.Promocion.Tipo == tipo).first()

# Buscar todas las promociones con paginación
def get_promociones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.promociones.Promocion).offset(skip).limit(limit).all()

# Crear una nueva promoción
def create_promocion(db: Session, promocion: schemas.promociones.PromocionCreate):
    db_promocion = models.promociones.Promocion(
        Producto_id=promocion.Producto_id,
        Tipo=promocion.Tipo,
        Aplicacion_en=promocion.Aplicacion_en,
        Estatus=promocion.Estatus,
        Fecha_Registro=promocion.Fecha_Registro,
        Fecha_Actualizacion=promocion.Fecha_Actualizacion
    )
    db.add(db_promocion)
    db.commit()
    db.refresh(db_promocion)
    return db_promocion

# Actualizar una promoción por ID
def update_promocion(db: Session, id: int, promocion: schemas.promociones.PromocionUpdate):
    db_promocion = db.query(models.promociones.Promocion).filter(models.promociones.Promocion.ID == id).first()
    if db_promocion:
        for var, value in vars(promocion).items():
            if value is not None:
                setattr(db_promocion, var, value)
        db.commit()
        db.refresh(db_promocion)
    return db_promocion

# Eliminar una promoción por ID
def delete_promocion(db: Session, id: int):
    db_promocion = db.query(models.promociones.Promocion).filter(models.promociones.Promocion.ID == id).first()
    if db_promocion:
        db.delete(db_promocion)
        db.commit()
    return db_promocion
