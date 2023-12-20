from contextlib import asynccontextmanager
from uvicorn import Config, Server

from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger

import events.api as events_api
import localizations.api as localization_api
import healthcheck.api as healthcheck_api

from db import init_db
from auth import register_auth_routers


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

#checar si rompe borrar
def run():
    app = create_app()

    # Set up Uvicorn configuration for enhanced logging
    config = Config(app, log_level="info", reload=True)

    # Create the Uvicorn server
    server = Server(config)

    # Start the server
    fastapi_logger.info("Starting Uvicorn server")
    server.run()


# If the script is executed directly, run the FastAPI application
if __name__ == "__main__":
    run()


#app = create_app()