
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length= 50)
    email: EmailStr
    phone: str = Field(min_length= 9, max_length= 15)
    age: Optional[int] = None
    
    
    
class User(UserCreate):
    _id_count = 1
    id: int
    active: bool
    
    def __init__(self):
        User._id_count += 1