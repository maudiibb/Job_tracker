from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.schemas import Company, Application
from app.database import get_db


app = FastAPI()

@app.post("/companies/", response_model=Company)
def creat_company_endpoint(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db, company)