from pydantic import BaseModel
from typing import Optional

class BikeBase(BaseModel):
    basket: Optional[bool] = None
    type_id: int


class BikeCreate(BikeBase):
    user_id: int
    color: Optional[str] = None


class BikeResponse(BikeBase):
    id: int
    user_id: int
    color: Optional[str]

    model_config = {
        "from_attributes": True
    }