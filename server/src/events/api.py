from fastapi import APIRouter, status

from events import crud
from events.schemas import CreateEvent, ResponseEvent

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/")
async def get_events():
    events = await crud.get_events()

    return events


@router.post("/", response_model=ResponseEvent, status_code=status.HTTP_201_CREATED)
async def create_event(event: CreateEvent):
    return event
