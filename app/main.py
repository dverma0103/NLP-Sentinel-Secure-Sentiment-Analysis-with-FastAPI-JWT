from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import engine, SessionLocal
from auth import create_access_token, verify_access_token
from schemas import Base, Token, UserCreate, AnalyserCreate, AnalyserOut, User
from user import create_user, get_users, authenticate_user
from sentiment_analyser import get_all_analysis, create_analyser, delete_analysis
import time

Base.metadata.create_all(engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.middleware("http")
async def logginin(request:Request, call_next):
    start_time = time.time()
    response = await call_next(call_next)
    processed_time = time.time() - start_time
    print(f"{request.method} {request.url.path} completed in {processed_time:.2f} seconds")
    return response

@app.post("/signup")
async def signup(user:UserCreate, db:Session = Depends(get_db)):
    if get_users(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    create_user(db, user)
    return {"message": "User created successfully"}

@app.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token:str = Depends(oauth2_scheme), db:Session = Depends(get_db)):
    username = verify_access_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = get_users(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid User")
    return user

@app.post("/analysis", response_model=AnalyserOut)
async def create_analysis(analyser:AnalyserCreate, current_user: User = Depends(get_current_user), db:Session = Depends(get_db)):
    return create_analyser(db, analyser, current_user.id)

@app.get("/analysis", response_model=list[AnalyserOut])
async def get_all_analysis_by_user(current_user: User = Depends(get_current_user), db:Session = Depends(get_db)):
    return get_all_analysis(db, current_user.id)

@app.delete("/analysis/{analysis_id}")
async def delete_user_analysis(analysis_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    delete_analysis(db, analysis_id, current_user.id)
    return {"message": "Analysis Deleted"}