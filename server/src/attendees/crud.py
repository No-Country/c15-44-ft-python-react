from .models import EventAttendees
from fastapi import HTTPException, status
from sqlmodel import Session,select, delete
from src.db import engine

async def get_attendees_by_event(event_id):
    with Session(engine) as session:
        query = select(EventAttendees).where(EventAttendees.id == event_id)
        attendees = session.exec(query).all()
        if not attendees:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No event not found with this id: {event_id}"
            )
    return attendees


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

async def create_event_attendee(attendee, event_id):
    try:
        with Session(engine) as session:
            new_event=EventAttendees(user_id=attendee, event_id = event_id)
            session.add(new_event)
            session.commit()
            session.refresh(new_event)
        return new_event
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Failed to create event: {str(e)}")


async def delete_attendee(user_id = int, event_id = int):
    with Session(engine) as session:
        query = select(EventAttendees).where(EventAttendees.event_id == event_id, EventAttendees.user_id == user_id)
        event = session.exec(query).all()
        if not event:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Event not found")
        try:
            session.exec(delete(EventAttendees).where(EventAttendees.event_id == event_id, EventAttendees.user_id == user_id))
            session.commit()
            return event
        except Exception as e:
            session.rollback()
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"Failed to delete event: {str(e)}")
