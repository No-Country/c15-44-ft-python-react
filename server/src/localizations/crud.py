from sqlmodel import Session
from sqlalchemy import Engine
from models import Localization
from db import get_engine

all_localizations = [
    {
        "country": "Argentina",
        "country_id": 1,
        "province": "Buenos Aires"
    },
    {
        "country": "Argentina",
        "country_id": 1,
        "province": "Mendoza"
    },
    {
        "country": "France",
        "country_id": 2,
        "province": "Paris"
    },
]

#all countries - no provinces
async def get_countries(engine: Engine = Depends(get_engine)):
    
    with Session(engine) as session:
        all_countries = session.get(Localization)
    
    unique_countries = set()
    countries = [
        {"country": country["country"], "id": country["id"]} 
        for country in all_countries 
        if country["country"] not in unique_countries and (unique_countries.add(country["country"]) or True)
        ]
    
    return countries

#provinces for specified country
async def get_provinces_bycountryid(country_id):
    provinces_bycountry = [province for province in all_localizations if province["country_id"] == country_id]
    return provinces_bycountry


#country + all provinces

#create country and province
async def post_country(country):
    return country

#create province for existing country
async def post_country(province):
    return province

#delete country and or province

#update country

#update province