from app.database import SessionLocal
from app.models import Company, Application
from datetime import date

# Öppna en session (ett "samtal" med databasen)
db = SessionLocal()

# Skapa ett nytt företag
new_company = Company(
    name="Formpipe",
    website="https://www.formpipe.com",
    industry="Software"
)

db.add(new_company)      # markera att den ska sparas
db.commit()              # spara faktiskt till databasen
db.refresh(new_company)  # hämta tillbaka objektet, nu med sitt tilldelade id

print(f"Skapade företag: {new_company.name} med id {new_company.id}")

# Skapa en ansökan kopplad till det företaget
new_application = Application(
    company_id=new_company.id,
    role_title="Junior Developer",
    status="applied",
    applied_date=date.today(),
    source="LinkedIn"
)

db.add(new_application)
db.commit()
db.refresh(new_application)

print(f"Skapade ansökan: {new_application.role_title} (status: {new_application.status})")

# Nu testar vi relationen - hämta alla ansökningar för detta företag
company_from_db = db.query(Company).filter(Company.name == "Formpipe").first()
print(f"\n{company_from_db.name} har {len(company_from_db.applications)} ansökan/ansökningar:")
for app in company_from_db.applications:
    print(f" - {app.role_title} ({app.status})")

db.close()