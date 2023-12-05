from typing import Annotated
from pydantic import BaseModel, Field

class CreateCountry(BaseModel):
    country: Annotated[str, Field(min_length=3)]
    province: str

class LocalizationModel(BaseModel):
    country: Annotated[str, Field(min_length=3)]
    country_id: int
    
class ResponseProvince(LocalizationModel):
    province: Annotated[str, Field(min_length=3)]