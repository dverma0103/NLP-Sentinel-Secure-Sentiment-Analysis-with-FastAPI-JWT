from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

secret_key = os.getenv("SECRET_KEY")
algorithm = "HS256"
expiry_time = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expiry_time)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)

def verify_access_token(token:str):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        return payload.get("sub")
    except JWTError:
        return None