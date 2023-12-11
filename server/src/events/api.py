from fastapi import APIRouter, status

from events import crud
from events.schemas import CreateEvent, ResponseEvent
from .models import Event

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/")
async def get_events(country_id: int):
    events = await crud.get_all_events(country_id)
    return events

@router.get("/{event_id}")
async def get_event(event_id: int):
    events = await crud.get_event_by_id(event_id)
    return events

@router.get("country/{country_id}/province/{province_id}")
async def get_eventsbyprovince(country_id: int,province_id: int):
    events = await crud.get_events_by_province(country_id,province_id)
    return events

@router.get("/{event_id}/images")
async def get_eventimg(event_id: int):
    imagesurl = await crud.get_event_images(event_id)
    return imagesurl


@router.post("/", response_model=ResponseEvent, status_code=status.HTTP_201_CREATED)
async def create_event(event: Event):
    eventc = await crud.create_event(event)
    return eventc

@router.put("/")
async def update_event(event: Event):
    updevent = await crud.update_event_by_id(event)
    return updevent
