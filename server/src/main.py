from contextlib import asynccontextmanager
from uvicorn import Config, Server

from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
from fastapi.middleware.cors import CORSMiddleware

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


    # Add CORS middleware
    origins = [
        "http://18.231.163.164:8000/",
        "https://18.231.163.164:8000/",
        "http://18.231.163.164:80/"
        "https://18.231.163.164:80/",
        # Add more origins as needed
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_auth_routers(app)
    app.include_router(healthcheck_api.router)
    app.include_router(events_api.router)
    app.include_router(localization_api.router)

    return app

app = create_app()