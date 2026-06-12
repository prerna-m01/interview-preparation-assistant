from src.database.models import Base
from src.database.session import engine

Base.metadata.create_all(bind=engine)

print("Database created successfully")