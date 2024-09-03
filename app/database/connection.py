from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Load environment variables from a .env file or system environment variables
#DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test3.db")
DATABASE_URL = "postgresql://procure:Farm1234$@farmdb.postgres.database.azure.com/procure"

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL, echo=True
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our models
Base = declarative_base()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database
def init_db():
    # Import all the models here so they are registered on the Base.metadata
    
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)