from typing import List

from fastapi import APIRouter, status, Depends
from . import crud
from .schemas import ResponseProvince, CreateCountry
from .models import Province, Country

router = APIRouter(prefix="/localization", tags=["localization"])

@router.get("/country")
async def get_all_countries():
    all_localizations = await crud.get_countries()
    return all_localizations

@router.get("/country/{country_id}/provinces", response_model=List[Province] )
async def get_provinces_bycountryid(country_id: int):
    provincesByCountry = await crud.get_provinces_bycountryid(country_id)
    return provincesByCountry

@router.post("/country", status_code=status.HTTP_201_CREATED)
async def create_country(country: CreateCountry):
    createdCountry = await crud.post_country(country)
    return createdCountry

@router.post("/country/{country_id}/provinces",status_code=status.HTTP_201_CREATED)
async def create_province(province: ResponseProvince):
    createProvince = await crud.post_province(province)
    return createProvince

@router.delete("/country/{country_id}")
async def delete_country(country_id: int):
    deletedCountry = await crud.delete_countrybyid(country_id)
    return deletedCountry
    

