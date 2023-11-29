from contextlib import asynccontextmanager

from fastapi import FastAPI

import events.api as eventsApi

from .api import healthcheck
from .db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


def create_app():
    app = FastAPI(debug=True, lifespan=lifespan)

    app.include_router(healthcheck.router)
    app.include_router(eventsApi.router)

    return app


app = create_app()
