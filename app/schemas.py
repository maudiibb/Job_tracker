from pydantic import BaseModel
from datetime import date
from typing import Optional

# --- Company scheman ---

class CompanyBase(BaseModel):
    name: str
    website: Optional[str] = None
    industry: Optional[str] = None
    notes: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass  # samma fält som CompanyBase, men egen klass för tydlighet vid skapande

class Company(CompanyBase):
    id: int

    class Config:
        from_attributes = True  # låter Pydantic läsa data direkt från SQLAlchemy-objekt


# --- Application scheman ---

class ApplicationBase(BaseModel):
    role_title: str
    status: str = "saved"
    applied_date: Optional[date] = None
    source: Optional[str] = None
    job_url: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    company_id: int  # måste anges vid skapande

class Application(ApplicationBase):
    id: int
    company_id: int
    warning: str | None = None

    class Config:
        from_attributes = True

class CompanyWithApplications(Company):
    applications: list[Application] = []