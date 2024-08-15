from fastapi import  Depends,APIRouter, HTTPException
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.miembros
import crud.miembros, config.db, schemas.miembros, models.miembros
from typing import List
from portadortoken import Portador


key=Fernet.generate_key()
f = Fernet(key)

miembros = APIRouter()

models.membresias.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@miembros.get("/miembros/", response_model=List[schemas.miembros.Miembro], tags=["Miembros"],dependencies=[Depends(Portador())] )
def read_miembros(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users= crud.miembros.get_miembros(db=db, skip=skip, limit=limit)
    return db_users

@miembros.post("/miembro/{id}", response_model=schemas.miembros.Miembro, tags=["Miembros"],dependencies=[Depends(Portador())])
def read_miembro(id: int, db: Session = Depends(get_db)):
    db_user= crud.miembros.get_miembro(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_user

@miembros.post("/miembro/", response_model=schemas.miembros.Miembro, tags=["Miembros"])
def create_miembro(miembro: schemas.miembros.MiembroCreate, db: Session = Depends(get_db)):
    db_user = crud.miembros.get_miembro_by_id(db, tipo=miembro.Tipo)
    if db_user:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")
    return crud.miembros.create_miembros(db=db, nom=miembro)

@miembros.put("/miembro/{id}", response_model=schemas.miembros.Miembro, tags=["Miembros"],dependencies=[Depends(Portador())])
def update_miembro(id: int, persona: schemas.miembros.MiembroUpdate, db: Session = Depends(get_db)):
    db_user = crud.miembros.update_miembros(db=db, id=id, person=persona)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizado")
    return db_user

@miembros.delete("/miembro/{id}", response_model=schemas.miembros.Miembro, tags=["Miembros"],dependencies=[Depends(Portador())])
def delete_miembro(id: int, db: Session = Depends(get_db)):
    db_user = crud.miembros.delete_miembros(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_user