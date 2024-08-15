from fastapi import  Depends,APIRouter, HTTPException
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.membresias
import crud.membresias, config.db, schemas.membresias, models.membresias
from typing import List
from portadortoken import Portador


key=Fernet.generate_key()
f = Fernet(key)

membresia = APIRouter()

models.membresias.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@membresia.get("/membresias/", response_model=List[schemas.membresias.Membresia], tags=["Membresias"],dependencies=[Depends(Portador())] )
def read_membresias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users= crud.membresias.get_membresias(db=db, skip=skip, limit=limit)
    return db_users

@membresia.post("/membresia/{id}", response_model=schemas.membresias.Membresia, tags=["Membresias"],dependencies=[Depends(Portador())])
def read_membresia(id: int, db: Session = Depends(get_db)):
    db_user= crud.membresias.get_membresia(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_user

@membresia.post("/membresia/", response_model=schemas.membresias.Membresia, tags=["Membresias"],dependencies=[Depends(Portador())])
def create_membresia(membresia: schemas.membresias.MembresiaCreate, db: Session = Depends(get_db)):
    db_user = crud.membresias.get_membresia_by_id(db, codigo=membresia.Codigo)
    if db_user:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")
    return crud.membresias.create_membresias(db=db, nom=membresia)

@membresia.put("/membresia/{id}", response_model=schemas.membresias.Membresia, tags=["Membresias"],dependencies=[Depends(Portador())])
def update_membresia(id: int, persona: schemas.membresias.MembresiaUpdate, db: Session = Depends(get_db)):
    db_user = crud.membresias.update_membresias(db=db, id=id, person=persona)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizado")
    return db_user

@membresia.delete("/membresia/{id}", response_model=schemas.membresias.Membresia, tags=["Membresias"],dependencies=[Depends(Portador())])
def delete_membresia(id: int, db: Session = Depends(get_db)):
    db_user = crud.membresias.delete_membresias(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_user