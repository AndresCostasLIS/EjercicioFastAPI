
from itertools import count
from typing import ClassVar, Optional
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length= 50)
    email: EmailStr
    phone: str = Field(min_length= 9, max_length= 15)
    age: Optional[int] = None
    
    def create_user(self) -> "User":
        return User(**self.model_dump())
    
    
class User(UserCreate):
    _id_counter: ClassVar[count] = count(1)
    id: int = Field(default_factory=lambda: next(User._id_counter))
    active: bool = True
    
class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, min_length=9, max_length=15)
    age: Optional[int] = None
    active: Optional[bool] = None