from typing import Optional

from sqlmodel import Field, SQLModel

class Localization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    country: str = Field(max_length=30, min_length=3)
    province: str = Field(max_length=30, min_length=3)