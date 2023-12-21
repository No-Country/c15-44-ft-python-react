from contextlib import asynccontextmanager
from uvicorn import Config, Server

from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger

from .events import api as events_api
from .localizations import api as localization_api
from .healthcheck import api as healthcheck_api

from .db import init_db
from .auth import register_auth_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    fastapi_logger.info("Initializing database")
    init_db()
    fastapi_logger.info("Database initialization complete")
    yield


def create_app():
    app = FastAPI(debug=True, lifespan=lifespan)

    register_auth_routers(app)
    app.include_router(healthcheck_api.router)
    app.include_router(events_api.router)
    app.include_router(localization_api.router)

    return app

app = create_app()