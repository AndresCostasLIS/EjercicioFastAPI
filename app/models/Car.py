from typing import Optional

from pydantic import Field
from app.api.models import Vehicle

class Car(Vehicle):
    plate: str = Field(min_length= 7 ,max_length = 30)
    capacity: Optional[int]
    electrical: Optional[bool]