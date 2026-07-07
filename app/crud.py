from sqlalchemy.orm import Session
from app import models, schemas
from app.models import Company, Application

def get_company(db: Session, company_id: int):
    result = db.query(Company).filter(Company.id == company_id ).first()
    return result

def get_companies(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(Company).offset(skip).limit(limit).all()
    return result

def create_company(db: Session, company: schemas.CompanyCreate):
    new_company = Company(
        name = company.name, 
        website = company.website, 
        industry = company.industry,
        notes = company.notes
    )

    db.add(new_company)      # markera att den ska sparas
    db.commit()              # spara faktiskt till databasen
    db.refresh(new_company)  # hämta tillbaka objektet, nu med sitt tilldelade id
    return new_company

def get_application(db: Session, application_id: int):
    result = db.query(Application).filter(Application.id == application_id).first()
    return result

def get_applications(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(Application).offset(skip).limit(limit).all()
    return result

def create_application(db: Session, application: schemas.ApplicationCreate):
    new_application = Application(
        company_id = application.company_id,
        role_title = application.role_title,
        status = application.status,
        applied_date = application.applied_date,
        source = application.source,
        job_url = application.job_url
    )

    db.add(new_application)         # markera att den ska sparas
    db.commit()                     # spara faktiskt till databasen
    db.refresh(new_application)     # hämta tillbaka objektet, nu med sitt tilldelade id
    return new_application
