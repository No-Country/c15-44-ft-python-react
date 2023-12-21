from fastapi import APIRouter, status

from . import crud
from .models import EventAttendees

router = APIRouter(prefix="/attendees", tags=["attendees"])

@router.get("/{event_id}")
async def get_attendees(event_id: int):
    attendees = await crud.get_attendees_by_event(event_id)
    return attendees

@router.post("/{event_id}/user/{user_id}", status_code=status.HTTP_201_CREATED)
async def create_attendee(attendee: int, event_id: int):
    eventattendee = await crud.create_event_attendee(attendee, event_id)
    return eventattendee

@router.delete("/{event_id}/user/{user_id}")
async def update_event(user_id: int, event_id: int):
    delattendee = await crud.delete_attendee(user_id, event_id)
    return delattendee
