from models import SQLModel
from database import engine

# Create all tables in the database
print("Creating tables...")
SQLModel.metadata.create_all(bind=engine)
print("Tables created successfully!")