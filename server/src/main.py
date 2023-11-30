from contextlib import asynccontextmanager

from fastapi import FastAPI

import events.api as eventsApi
import localizations.api as localizationApi

import api.healthcheck as healthcheckApi
from src.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


def create_app():
    app = FastAPI(debug=True, lifespan=lifespan)

    app.include_router(healthcheckApi.router)
    app.include_router(eventsApi.router)
    app.include_router(localizationApi.router)

    return app


app = create_app()
