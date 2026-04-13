from itertools import count

from pydactic import BaseModel
from typing import ClassVar, Field


class TypeCreate(BaseModel):
    
    description: str = Field(max_length= 150)
    
class Type(TypeCreate):
    _id_counter: ClassVar[count] = count(1)
    id: int = Field(default_factory=lambda: next(Type._id_counter))

        
    
        
        

    