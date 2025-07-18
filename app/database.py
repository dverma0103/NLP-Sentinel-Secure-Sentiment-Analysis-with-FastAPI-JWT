from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()