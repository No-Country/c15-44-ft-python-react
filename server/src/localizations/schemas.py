from typing import Annotated
from pydantic import BaseModel, Field

class CreateCountry(BaseModel):
    name: Annotated[str, Field(min_length=3)]

class LocalizationModel(BaseModel):
    country: Annotated[str, Field(min_length=3)]
    country_id: int
    
class ResponseProvince(LocalizationModel):
    province: Annotated[str, Field(min_length=3)]