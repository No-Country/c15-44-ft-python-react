from fastapi import APIRouter, status

from . import crud
from .schemas import CreateEvent, ResponseEvent
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
async def get_events_by_province(country_id: int,province_id: int):
    events = await crud.get_events_by_province(country_id,province_id)
    return events

@router.get("country/{country_id}")
async def get_events_by_province(country_id: int,province_id: int):
    events = await crud.get_events_by_country(country_id,province_id)
    return events

@router.get("country/{country_id}/category/{category_id}")
async def get_events_by_coutnry_by_category(country_id: int,category_id: int):
    events = await crud.get_events_by_country_category(country_id,category_id)
    return events

@router.get("/category/{category_id}")
async def get_events_by_category(category_id: int):
    events = await crud.get_events_by_category(category_id)
    return events

@router.get("/{event_id}/images")
async def get_eventimg(event_id: int):
    imagesurl = await crud.get_event_images(event_id)
    return imagesurl


@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_event(event: Event):
    eventc = await crud.create_event(event)
    return eventc

@router.put("/")
async def update_event(event: Event):
    updevent = await crud.update_event_by_id(event)
    return updevent

@router.delete("/{event_id}")
async def delete_event(event_id: int):
    deletedevent = await crud.delete_event_by_id(event_id)
    return deletedevent
