from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from . import crud, models, schemas
from . database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_schema)):
    return {"token": token}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_items(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}