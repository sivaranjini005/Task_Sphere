from sqlmodel import create_engine, Session
from sqlalchemy.orm import sessionmaker

database_url = "postgresql://postgres:admin@localhost:5432/task_manager"

engine = create_engine(database_url, echo = True)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind= engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
        
    finally:
        db.close()