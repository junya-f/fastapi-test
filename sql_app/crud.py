from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import models, schemas
from fastapi import HTTPException

#user情報の取得
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

#user登録
def create_user(db: Session, user: schemas.CreateUser):
    fake_hashed_password = user.hashed_password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#todoリスト一覧の取得
def get_todo_lists(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Todo_list).offset(skip).limit(limit).all()

#todoリスト作成
def create_todo_lists(db: Session, todo_lists: schemas.CreateTodo):
    db_todo_lists = models.Todo_list(title=todo_lists.title, content=todo_lists.content)
    db.add(db_todo_lists)
    db.commit()
    db.refresh(db_todo_lists)
    return db_todo_lists

#todoリスト更新
def update_todo_lists(db: Session, todo_id: int, todo_update: schemas.UpdateTodo):
    todo = db.query(models.Todo_list).filter(models.Todo_list.todo_id == todo_id).first()
    if not todo:
        return None
    todo_data = todo_update.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

#todoリストの削除
def deleate_todo(db: Session, todo_id: int):
    todo = db.query(models.Todo_list).filter(models.Todo_list.todo_id == todo_id).first() 
    if not todo:
        return None
    db.deleate(todo)
    db.commit()
    return todo