from sqlalchemy.orm import Session
from schemas import User, UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def get_users(db:Session, username:str):
    return db.query(User).filter(User.username == username).first()

def create_user(db:Session, user:UserCreate):
    hashed_pass = pwd_context.hash(user.password)
    user_db = User(username = user.username, hashed_password = hashed_pass)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def authenticate_user(db:Session, username: str, password: str):
    user = get_users(db, username)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user