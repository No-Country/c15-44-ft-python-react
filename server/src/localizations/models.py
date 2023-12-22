from typing import Optional

from sqlmodel import Field, SQLModel

class Country(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30, min_length=3)
    
class Province(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    province: str
    country_id: int = Field(foreign_key="country.id")
    country: str