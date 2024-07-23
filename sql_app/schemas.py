import datetime
from pydantic import BaseModel, Field

#users

class CreateUser(UserBase):
    user_id: int
    email: str
    username: str = Field(max_length=12)
    
class ReadUser(Usercreate):
    
    
#todo_lisus
class TodoBase(BaseModel):
    title: str
    content: str
    
class CreateTodo(TodoBase):
    todo_id: int
    completed: bool
    
class ReadTodo

class UpdateTodo
    
    