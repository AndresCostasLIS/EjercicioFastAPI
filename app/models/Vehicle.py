from itertools import count
from typing import ClassVar

from app.models.User import User
from pydantic import BaseModel, Field

class VehicleCreate(BaseModel):
    
    color: str = Field(min_length=3, max_length= 25)



class Vehicle(VehicleCreate):
    _id_counter: ClassVar[count] = count(1)
    id: int = Field(default_factory=lambda: next(Vehicle._id_counter))
    active: bool= True
    