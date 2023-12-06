from typing import Optional

from sqlmodel import Field, SQLModel


class EventAttendees(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    event_id: int