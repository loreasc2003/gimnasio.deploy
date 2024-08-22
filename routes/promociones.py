from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.promociones, config.db, schemas.promociones, models.promociones
from typing import List
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

promocion = APIRouter()
models.promociones.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todas las promociones
@promocion.get('/promociones/', response_model=List[schemas.promociones.Promocion], tags=['Promociones'], dependencies=[Depends(Portador())])
def read_promociones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_promociones = crud.promociones.get_promociones(db=db, skip=skip, limit=limit)
    return db_promociones

# Ruta para obtener una promoción por ID
@promocion.get("/promociones/{id}", response_model=schemas.promociones.Promocion, tags=["Promociones"], dependencies=[Depends(Portador())])
def read_promocion(id: int, db: Session = Depends(get_db)):
    db_promocion = crud.promociones.get_promocion(db=db, id=id)
    if db_promocion is None:
        raise HTTPException(status_code=404, detail="Promoción no encontrada")
    return db_promocion

# Ruta para crear una promoción
@promocion.post('/promociones/', response_model=schemas.promociones.Promocion, tags=['Promociones'])
def create_promociones(promocion: schemas.promociones.PromocionCreate, db: Session = Depends(get_db)):
    # Busca promociones existentes con el mismo tipo
    db_promociones = crud.promociones.get_promocion_by_tipo(db, tipo=promocion.Tipo)
    if db_promociones:
        # Lanza una excepción si ya existe una promoción con el mismo tipo
        raise HTTPException(status_code=400, detail="Promoción existente, intenta nuevamente")
    # Crea la nueva promoción y la guarda en la base de datos
    return crud.promociones.create_promocion(db=db, promocion=promocion)

# Ruta para actualizar una promoción
@promocion.put('/promociones/{id}', response_model=schemas.promociones.Promocion, tags=['Promociones'], dependencies=[Depends(Portador())])
def update_promociones(id: int, promocion: schemas.promociones.PromocionUpdate, db: Session = Depends(get_db)):
    db_promocion = crud.promociones.update_promocion(db=db, id=id, promocion=promocion)
    if db_promocion is None:
        raise HTTPException(status_code=404, detail="Promoción no encontrada, no se pudo actualizar")
    return db_promocion

# Ruta para eliminar una promoción
@promocion.delete('/promociones/{id}', response_model=schemas.promociones.Promocion, tags=['Promociones'], dependencies=[Depends(Portador())])
def delete_promociones(id: int, db: Session = Depends(get_db)):
    db_promocion = crud.promociones.delete_promocion(db=db, id=id)
    if db_promocion is None:
        raise HTTPException(status_code=404, detail="Promoción no encontrada, no se pudo eliminar")
    return db_promocion
