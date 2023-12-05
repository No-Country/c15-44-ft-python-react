from typing import Optional

from sqlmodel import Field, SQLModel,Relationship

class Country(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30, min_length=3)
class Province(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    province: str
    country_id: int = Field(foreign_key="country.id")
    country: Relationship = Relationship(back_populates="provinces")

#class Localization(SQLModel, table=True):
#    id: Optional[int] = Field(default=None, primary_key=True)
#    province_id: int = Field(foreign_key="province.id")
#    country_id:int = Field(foreign_key="country.id") 

#class Localization(SQLModel, table=True):
 #   id: Optional[int] = Field(default=None, primary_key=True)
  #  country: Relationship = Relationship(back_populates="localizations")
  #  province_id: int = Field(foreign_key="province.id")
  #  country_id:int = Field(foreign_key="country.id") 
  #  province: Relationship = Relationship(back_populates="localizations")