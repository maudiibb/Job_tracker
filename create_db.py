from app.database import engine, Base
from app import models

# Detta läser alla klasser som ärver från Base (dvs. Company och Application)
# och skapar motsvarande tabeller i databasen
Base.metadata.create_all(bind=engine)

print("Databasen och tabellerna skapades!")