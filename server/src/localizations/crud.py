from fastapi import Depends, HTTPException, status
from http import HTTPStatus
from sqlmodel import Session, select, func, delete
from sqlalchemy import Engine
from .models import Country, Province
from src.db import engine

#all countries - no provinces
async def get_countries():
    with Session(engine) as session:
        query = select(Country)
        result = session.exec(query)
        countries = [{"name": country.name, "id": country.id} for country in result]
    return countries

#get provinces for specified country
async def get_provinces_bycountryid(country_id):
    with Session(engine) as session:
        query = select(Province).where(Province.country_id == country_id)
        provinces = session.exec(query).all()
        if not provinces:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Provinces not found for Country ID: {country_id}"
            )
    return provinces

#create country
async def post_country(country):
    with Session(engine) as session:
        existing_country = session.exec(select(Country).where(func.lower(Country.name) == country.name.lower())).first()
        if existing_country:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Country with this name already exists")
        
        new_country=Country(name=country.name)
        session.add(new_country)
        session.commit()
        session.refresh(new_country)
        
    return new_country

#create province for existing country
async def post_province(province):
    with Session(engine) as session:
        existing_country = session.exec(select(Country).where(Country.id == province.country_id)).first()
        if not existing_country:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")

        existing_province = session.exec(
            select(Province)
            .where((func.lower(Province.province) == province.province.lower()) & (Province.country_id == province.country_id))
        ).first()
        
        if existing_province:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Province with this name already exists for the country")

        new_province = Province(province=province.province, country_id=province.country_id, country = existing_country.name)
        session.add(new_province)
        session.commit()
        session.refresh(new_province)
        
    return new_province

#delete country and or province
async def delete_countrybyid(country_id: int):
    with Session(engine) as session:
        country = session.get(Country, country_id)
        if not country:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Country not found")
        try:
            session.exec(delete(Province).where(Province.country_id == country_id))
            session.exec(delete(Country).where(Country.id == country_id))
            session.commit()
            return country
        except Exception as e:
            session.rollback()
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"Failed to delete country: {str(e)}")
#update country

#update province