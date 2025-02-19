from sqlmodel import SQLModel, Field,  Relationship
from sqlalchemy import Column, DateTime, func
from typing import Optional, List
from datetime import datetime, date

# pydantic models 
class UserBase(SQLModel):
    id:int
    name:str
    email: str

class TaskResponse(SQLModel):
    id:int
    title: str 
    description: Optional[str]=None
    deadline:Optional[date] = None
    is_completed: bool

class UserResponse(UserBase):
    tasks: List[TaskResponse] = []

class UserCreate(SQLModel):
    name: str
    email: str
    password: str

class Taskcreate(SQLModel):
    title: str
    description: Optional[str] = None
    deadline:Optional[date] = None
    is_completed: bool = Field(default = False)
    


#sql models for database
class User(SQLModel, table = True):
    __tablename__ = 'users'
    id:Optional[int] = Field(default = None, primary_key= True)
    name:str = Field(nullable = False)
    email:str = Field(unique= True)
    password: str
    created_at: datetime= Field(default_factory = datetime.utcnow)
    updated_at: datetime = Field(sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow))
    tasks: List["Task"] = Relationship(back_populates = "user")

class Task(SQLModel, table = True):
    __tablename__ = "tasks"
    id: Optional[int] = Field(default = None, primary_key= True)
    title: str
    description: Optional[str] = None
    deadline: Optional[date] = None
    is_completed:bool = Field(default = False)
    created_at: datetime = Field(default_factory = datetime.utcnow)
    updated_at: datetime = Field(sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow))
    user_id :int = Field(foreign_key = 'users.id')
    user : "User" = Relationship(back_populates="tasks")

class UserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    deadline:Optional[date] = None
    is_completed: Optional[bool] = None

