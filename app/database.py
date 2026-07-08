from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Vi använder SQLite till att börja med - det är en enda fil, ingen server behövs.
# Kan byta till PostgreSQL senare utan att ändra resten av koden nämnvärt.
SQLALCHEMY_DATABASE_URL = "sqlite:///./jobbtracker.db"

#
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # krävs specifikt för SQLite
)

# SessionLocal är "fabriken" som skapar databas-sessioner (samtal med databasen)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base är basklassen som alla våra tabeller (i models.py) kommer ärva från
Base = declarative_base()

# Denna funktion används av FastAPI för att ge varje request en egen databas-session
# och se till att den stängs korrekt efteråt
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()