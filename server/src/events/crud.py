from .models import Event, EventImg
from fastapi import HTTPException, status
from sqlmodel import Session,select, delete
from src.db import engine

async def get_all_events(country_id):
    with Session(engine) as session:
        query = select(Event).where(Event.country_id == country_id)
        events = session.exec(query).all()
        if not events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No events found for this country: {country_id}"
            )
    return events


async def get_event_by_id(event_id: int):
    with Session(engine) as session:
        query = select(Event).where(Event.id == event_id)
        event = session.exec(query).all()
        if not event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No event found with this id: {event_id}"
            )
    return event


async def get_events_by_province(country_id: int, province_id: int):
    with Session(engine) as session:
        query = select(Event).where(Event.country_id == country_id & Event.province_id == province_id)
        events = session.exec(query).all()
        if not events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No events found in this province: {province_id} and country: {country_id}"
            )
    return events

async def get_events_by_country(country_id: int):
    with Session(engine) as session:
        query = select(Event).where(Event.country_id == country_id)
        events = session.exec(query).all()
        if not events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No events found for this country: {country_id}"
            )
    return events

async def get_events_by_country_category(country_id: int, category_id: int):
    with Session(engine) as session:
        query = select(Event).where(Event.country_id == country_id & Event.category_id == category_id)
        events = session.exec(query).all()
        if not events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No events found in this category: {category_id} and country: {country_id}"
            )
    return events

async def get_events_by_category(category_id: int):
    with Session(engine) as session:
        query = select(Event).where(Event.category_id == category_id)
        events = session.exec(query).all()
        if not events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No events found in this category: {category_id}"
            )
    return events

async def get_event_images(event_id: int):
    with Session(engine) as session:
        query = select(EventImg).where(EventImg.event_id == event_id)
        eventimages = session.exec(query).all()
        if not eventimages:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No url images found for this event: {event_id}"
            )
    return eventimages

async def create_event(event):
    try:
        with Session(engine) as session:
            new_event = Event(
                name=event.name,
                creator_id=event.creator_id,
                timestamp=event.timestamp,
                date_and_time=event.date_and_time,
                country_id=event.country_id,
                province_id=event.province_id,
                address=event.address,
                price=event.price,
                category_id=event.category_id,
            )
            session.add(new_event)
            session.commit()
            session.refresh(new_event)
        return new_event
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Failed to create event: {str(e)}")


async def delete_event_by_id(event_id: int):
    with Session(engine) as session:
        event = session.get(Event, event_id)
        if not event:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Event not found")
        try:
            session.exec(delete(EventImg).where(EventImg.event_id == event_id))
            session.exec(delete(Event).where(Event.id == event_id))
            session.commit()
            return event
        except Exception as e:
            session.rollback()
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"Failed to delete event: {str(e)}")



async def update_event_by_id(update_event):
    with Session(engine) as session:
        existing_event = session.get(Event, update_event.id)
        if not existing_event:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

        for field, value in update_event.dict(exclude_unset=True).items():
            setattr(existing_event, field, value)

        session.commit()
        session.refresh(existing_event)

    return existing_event
