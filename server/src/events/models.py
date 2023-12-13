from datetime import datetime
from typing import Optional, Annotated

from sqlmodel import Field, SQLModel

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Annotated[str, Field(min_length=2)]
    creator_id: int
    timestamp: datetime = datetime.utcnow()
    date_and_time: datetime
    country_id: int
    province_id: int
    address: str
    price: float
    category_id: int
    
class EventImg(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str
    event_id: int = Field(foreign_key="event.id")
