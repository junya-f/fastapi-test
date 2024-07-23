#DBに登録する情報
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(254), unique=True, index=True)
    user_name = Column(String(128), index=True)
    hashed_password = Column(String)
    
    todoList = relationship("Todo_list", back_populates="owner" )
    
class Todo_list(Base):
    __tablename__ = "todo_lists"
    
    todo_id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    completed = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="Todo_list")
    