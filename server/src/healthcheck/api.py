from fastapi import APIRouter

router = APIRouter(prefix="/healthcheck", tags=["healthcheck"])


@router.get("/")
def healthcheck():
    return {"status": "ok"}
