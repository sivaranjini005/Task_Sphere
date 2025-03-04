from sqlmodel import create_engine, Session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

Database_URL = os.getenv("database_url")

engine = create_engine(Database_URL, echo = True)


SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind= engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
        
    finally:
        db.close()