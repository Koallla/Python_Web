
from crud import *
from database import SessionLocal, engine, Base
from schemas import Comand, ComandCreate


from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List




Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.get("/", response_class=HTMLResponse)
async def download_comands(request: Request, db: Session = Depends(get_db)):
    comands = crud_download_comands(db)
    return templates.TemplateResponse("comands-table.html", {"request": request, "comands": comands})




@app.get("/comands/", response_model=List[Comand])
def get_comands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comands = crud_get_comands(db, skip=skip, limit=limit)
    return comands


@app.get("/comand/{comand_id}", response_model=Comand)
def get_comand(comand_id: int, db: Session = Depends(get_db)):
    comand = crud_get_comand(db, comand_id=comand_id)
    if comand is None:
        raise HTTPException(status_code=404, detail="Comand not found")
    return comand



@app.post("/comand/", response_model=Comand)
def create_comand(comand: ComandCreate, db: Session = Depends(get_db)):
    check_comand = crud_get_comand(db, comand_name=comand.name)
    if new_comand:
        raise HTTPException(status_code=400, detail="Comand already registered")
    return crud_create_comand(db=db, comand=comand)
