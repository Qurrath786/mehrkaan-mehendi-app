# create_tables.py
from sqlalchemy import inspect
from app.db import Base, engine

# Import all your models here
from app.models.user import User
# from app.models.design import Design   # Uncomment when you add Design model
# from app.models.other_model import OtherModel  # Add more as needed

def create_all_tables():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully!")

    # Inspect and list all tables
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tables in the database:", tables)

if __name__ == "__main__":
    create_all_tables()
