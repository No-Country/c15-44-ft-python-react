from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class CreateEvent(BaseModel):
    name: Annotated[str, Field(min_length=2)]
    date: datetime
    price: float


class ResponseEvent(CreateEvent):
    id: int
    country_id: str
    province_id: str
