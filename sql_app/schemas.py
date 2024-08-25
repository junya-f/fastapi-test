import datetime
from pydantic import BaseModel, Field

#user
class CreateUser(BaseModel):
    email: str
    username: str = Field(max_length=12)
    hashed_password: str
    
class User(CreateUser):
    user_id: int
    
    class Config:
        orm_mode = True
    
#todo_lisus
class CreateTodo(BaseModel):
    user_id: int
    title: str
    content: str
    completed: bool
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    
class Todo(CreateTodo):
    todo_id: int

class UpdateTodo(Todo):
    pass

    class Config:
        orm_mode = True
    
    