from fastapi import Depends
from sqlmodel import Session, select
from sqlalchemy import Engine
from .models import Country, Province
from db import engine

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
async def get_countries():
    with Session(engine) as session:
        query = select(Country)
        all_countries = session.exec(query)
    return [{"country": country["country"]} for country in all_countries]

#provinces for specified country
async def get_provinces_bycountryid(country_id):
    provinces_bycountry = [province for province in all_localizations if province["country_id"] == country_id]
    return provinces_bycountry


#country + all provinces

#create country and province
async def post_country(country):
    with Session(engine) as session:
        select.add(country)
        session.commit()
    return country

#create province for existing country
async def post_country(province):
    with Session(engine) as session:
        new_province = Province(name=Province["province"], country_id = Province["country_id"], country = Province["country"])
        select.add(new_province)
        session.commit()
    return province

#delete country and or province

#update country

#update province