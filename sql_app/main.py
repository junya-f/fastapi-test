from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from . import crud, models, schemas
from . database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

#サインアップ
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

#ログイン
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#todoの作成
@app.post("/users/{user_id}/todo_lists", response_model=schemas.Todo)
def create_todo(todo_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

#todoの表示
@app.get("/users/{user_id}/todo_lists/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id:int ):

#todoの削除

#todoの更新