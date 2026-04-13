# app/models/Type.py

from pydantic import BaseModel, Field

class TypeBase(BaseModel):
    description: str = Field(min_length=3, max_length=150)


class TypeCreate(TypeBase):
    pass


class TypeResponse(TypeBase):
    id: int

    model_config = {
        "from_attributes": True
    }