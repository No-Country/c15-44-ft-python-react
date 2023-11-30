from fastapi import APIRouter, status
from localizations import crud
from localizations.schemas import ResponseProvince, CreateCountry
from typing import List

router = APIRouter(prefix="/localization", tags=["localization"])

@router.get("/country")
async def get_all_countries():
    all_localizations = await crud.get_countries()

    return all_localizations

@router.post("/country", status_code=status.HTTP_201_CREATED)
async def create_country(country: CreateCountry):
    createdCountry = await crud.post_country(country)
    return createdCountry

@router.get("/country/{country_id}/provinces", response_model=List[ResponseProvince] )
async def get_provinces_bycountryid(country_id: int):
    provincesByCountry = await crud.get_provinces_bycountryid(country_id)
    return provincesByCountry

@router.post("/country/{country_id}/provinces",status_code=status.HTTP_201_CREATED)
async def create_province(province: ResponseProvince):
    createProvince = await crud.post_province(province)
    return createProvince



