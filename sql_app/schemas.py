import datetime
from pydantic import BaseModel, Field
from typing import List

#user
class CreateUser(BaseModel):
    email: str
    user_name: str = Field(max_length=12)
    password: str
    
class User(CreateUser):
    user_id: int
    
    class Config:
        orm_mode = True
    
#todo_lists
class TodoListBase(BaseModel):
    title: str

class CreateTodoList(TodoListBase):
    pass

class TodoList(TodoListBase):
    id: int
    owner_id: int
    items: List["TodoItem"] = []
    
    class Config:
        orm_mode = True   
 
#todo_items
class TodoItemBase(BaseModel):
    content: str
    completed: bool = False

class CreateTodoItem(TodoItemBase):
    pass

class TodoItem(TodoItemBase):
    id: int
    todo_list_id: int
    
    class Config:
        orm_mode = True