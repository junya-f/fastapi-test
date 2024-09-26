#DBに登録する情報
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(254), unique=True, index=True)
    user_name = Column(String(128), index=True)
    hashed_password = Column(String, nullable=False)
    
    #TodoListとの紐付け
    todo_lists = relationship("TodoList", back_populates="owner")
    
class TodoList(Base):
    __tablename__ = "todo_lists"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    #Userとの紐付け
    owner_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    owner = relationship("User", back_populates="todo_lists")

    #TodoItemと紐付け
    items = relationship("TodoItem", back_populates="list", cascade="all delete-orphan")   
    
class TodoItem(Base):
    __tablename__ = "todo_items"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    completed = Column(Boolean, default=False)
    
    #TodoListとの紐付け。一体多の設定
    todo_list_id = Column(Integer, ForeignKey("todo_lists.id"), nullable=False)
    list = relationship("TodoList", back_populates="items")    