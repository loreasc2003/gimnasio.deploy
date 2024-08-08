from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.adeudos,config.db, schemas.adeudos,models.adeudos
from typing import List

adeudo = APIRouter()

models.adeudos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@adeudo.get("/adeudos/", response_model=List[schemas.adeudos.Adeudo], tags=["Adeudos"] ,dependencies=[Depends(Portador())])
def read_adeudos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_adeudos= crud.adeudos.get_adeudos(db=db, skip=skip, limit=limit)
    return db_adeudos

@adeudo.post("/adeudo/{ID}", response_model=schemas.adeudos.Adeudo, tags=["Adeudos"] ,dependencies=[Depends(Portador())])
def read_adeudo(ID: int, db: Session = Depends(get_db)):
    db_adeudo= crud.adeudos.get_adeudo(db=db, ID=ID)
    if db_adeudo is None:
        raise HTTPException(status_code=404, detail="adeudo not found")
    return db_adeudo

@adeudo.post("/adeudos/", response_model=schemas.adeudos.Adeudo, tags=["Adeudos"])
def create_adeudo(adeudo: schemas.adeudos.AdeudoCreate, db: Session = Depends(get_db)):
    db_adeudo = crud.adeudos.get_adeudo_by_Nombre(db, Nombre=adeudo.Nombre)
    if db_adeudo:
        raise HTTPException(status_code=400, detail="adeudo existente intenta nuevamente")
    return crud.adeudos.create_adeudo(db=db, adeudo=adeudo)

@adeudo.put("/adeudo/{ID}", response_model=schemas.adeudos.Adeudo, tags=["Adeudos"] ,dependencies=[Depends(Portador())])
def update_adeudo(ID: int, adeudo: schemas.adeudos.AdeudoUpdate, db: Session = Depends(get_db)):
    db_adeudo = crud.adeudos.update_adeudo(db = db, ID = ID, adeudo = adeudo)
    if db_adeudo is None:
        raise HTTPException(status_code=404, detail="adeudo no existente, no esta actuaizado")
    return db_adeudo

@adeudo.delete("/adeudo/{ID}", response_model=schemas.adeudos.Adeudo, tags=["Adeudos"] ,dependencies=[Depends(Portador())])
def delete_adeudo(ID: int, db: Session = Depends(get_db)):
    db_adeudo = crud.adeudos.delete_adeudo(db = db, ID = ID)
    if db_adeudo is None:
        raise HTTPException(status_code=404, detail="adeudo no existe, no se pudo eliminar")
    return db_adeudo