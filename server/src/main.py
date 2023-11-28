from contextlib import asynccontextmanager
from fastapi import FastAPI

from api import healthcheck
from db import create_db_and_tables
import events


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


def create_app():
    app = FastAPI(debug=True, lifespan=lifespan)

    app.include_router(healthcheck.router)
    app.include_router(events.router)

    return app


app = create_app()
