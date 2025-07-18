from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from pydantic import BaseModel

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    texts = relationship("Analyser", back_populates="owner")

class Analyser(Base):
    __tablename__ = "analysers"
    id: Mapped[int] = mapped_column(primary_key=True)
    inputs: Mapped[str] = mapped_column(nullable=False)
    sentiment: Mapped[str] = mapped_column(nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner = relationship("User", back_populates="texts")

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class AnalyserCreate(BaseModel):
    inputs: str

class AnalyserOut(BaseModel):
    id: int
    sentiment: str

    class config:
        orm_mode = True