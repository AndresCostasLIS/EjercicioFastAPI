from pydantic import BaseModel, Field
from typing import Optional

class CarBase(BaseModel):
    plate: str = Field(min_length=7, max_length=30)
    capacity: Optional[int] = None
    electrical: Optional[bool] = None


class CarCreate(CarBase):
    user_id: int
    color: Optional[str] = None


class CarResponse(CarBase):
    id: int
    user_id: int
    color: Optional[str]

    model_config = {
        "from_attributes": True
    }