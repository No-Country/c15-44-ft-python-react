from fastapi import APIRouter, HTTPException, status

from events import crud
from events.schemas import CreateEvent, ResponseEvent


router = APIRouter(prefix="/events", tags=["events"])


@router.get("/")
async def get_events():
    events = await crud.get_events()

    if len(events) >= 500:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Too many events"
        )

    return events


@router.post("/", response_model=ResponseEvent, status_code=status.HTTP_201_CREATED)
async def create_event(event: CreateEvent):
    return event
