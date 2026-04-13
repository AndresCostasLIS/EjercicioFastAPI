
from typing import Optional

from app.api.models import Type, Vehicle


class Bike(Vehicle):
    basket: Optional[bool]
    type_id: Type