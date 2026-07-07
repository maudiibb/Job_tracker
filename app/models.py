from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import date

from app.database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    website = Column(String, nullable=True)
    industry = Column(String, nullable=True)
    notes = Column(Text, nullable=True)

    # Detta skapar en koppling: company.applications ger dig alla ansökningar för detta företag
    applications = relationship("Application", back_populates="company")


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    role_title = Column(String, nullable=False)
    status = Column(String, default="saved")  # t.ex. saved, applied, screening, interview, offer, rejected
    applied_date = Column(Date, nullable=True)
    source = Column(String, nullable=True)  # t.ex. LinkedIn, egen ansökan, rekryterare
    job_url = Column(String, nullable=True)

    # Motsvarande koppling åt andra hållet: application.company ger dig företaget
    company = relationship("Company", back_populates="applications")