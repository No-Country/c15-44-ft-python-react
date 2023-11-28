from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class CreateEvent(BaseModel):
    name: Annotated[str, Field(min_length=5)]
    date: datetime
    price: int


class ResponseEvent(CreateEvent):
    id: int
    test: str
