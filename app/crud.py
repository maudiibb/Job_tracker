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

def delete_company(db: Session, company_id: int):
    result = db.query(Company).filter(Company.id == company_id ).first()
    linked_application =  db.query(Application).filter(Application.company_id == company_id).first()
    if result is None:
        return None
    elif linked_application is not None:
        return(f"Unable to delete company {company_id} because it is attached to {linked_application.role_title}")
    else:
        company_name = result.name
        db.delete(result)
        db.commit()
        return(f"Successfully deleted: {company_name}")

def update_company(db: Session, company: schemas.CompanyCreate, company_id: int):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company is None: return None
    db_company.name = company.name
    db_company.website = company.website
    db_company.industry = company.industry
    db_company.notes = company.notes
         
    db.commit()              
    db.refresh(db_company) 
    return db_company
    
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

def delete_application(db: Session, application_id: int):
    result = db.query(Application).filter(Application.id == application_id ).first()
    if result is None:
        return None
    else:
        application_role_title = result.role_title
        db.delete(result)
        db.commit()
        return(f"Successfully deleted: {application_role_title}")

def update_application(db: Session, application: schemas.ApplicationCreate, application_id: int):
    db_application = db.query(Application).filter(Application.id == application_id).first()
    if db_application is None: return None

    db_application.company_id = application.company_id
    db_application.role_title = application.role_title
    db_application.status = application.status
    db_application.applied_date = application.applied_date
    db_application.source = application.source
    db_application.job_url = application.job_url

    db.commit()              
    db.refresh(db_application) 
    return db_application