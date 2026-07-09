from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.schemas import Company, Application
from app.database import get_db
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse    

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

@app.post("/companies/", response_model=Company)
def creat_company_endpoint(company: schemas.CompanyCreate, 
                           db: Session = Depends(get_db)):
    return crud.create_company(db, company)

@app.get("/companies/", response_model=List[Company])
def get_companies_endpoint(skip: int = 0, limit: int = 100, 
                            db: Session = Depends(get_db)):
    return crud.get_companies(db, skip, limit)

@app.get("/companies/{company_id}", response_model=Company)
def get_company_endpoint(company_id : int, 
                           db: Session = Depends(get_db)):
    return crud.get_company(db, company_id)

@app.delete("/companies/{company_id}", response_model=str)
def delete_company_endpoint(company_id : int, 
                           db: Session = Depends(get_db)):
    return crud.delete_company(db, company_id)

@app.put("/companies/{company_id}", response_model=Company,)
def update_company_endpoint(company_id : int,
                            company: schemas.CompanyCreate, 
                            db: Session = Depends(get_db)):
    return crud.update_company(db, company, company_id)

@app.post("/applications/", response_model=Application)
def creat_application_endpoint(application: schemas.ApplicationCreate, 
                           db: Session = Depends(get_db)):
    return crud.create_application(db, application)

@app.get("/applications/", response_model=List[Application])
def get_applications_endpoint(skip: int = 0, limit: int = 100, 
                            db: Session = Depends(get_db)):
    return crud.get_applications(db, skip, limit)

@app.get("/applications/{application_id}", response_model=Application)
def get_application_endpoint(application_id: int, 
                           db: Session = Depends(get_db)):
    return crud.get_application(db, application_id)

@app.delete("/applications/{application_id}", response_model=str)
def delete_application_endpoint(application_id : int, 
                           db: Session = Depends(get_db)):
    return crud.delete_application(db, application_id)

@app.put("/applications/{application_id}", response_model=Application,)
def update_application_endpoint(application_id : int,
                            application: schemas.ApplicationCreate, 
                            db: Session = Depends(get_db)):
    return crud.update_application(db, application, application_id)