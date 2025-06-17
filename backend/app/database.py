from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://admin:root@db:5432/russian_food_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(expire_on_commit=False, autoflush=False, bind=engine)
Base = declarative_base()