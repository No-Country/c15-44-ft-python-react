from contextlib import asynccontextmanager

from fastapi import FastAPI

import events.api as events_api
import localizations.api as localization_api
import healthcheck.api as healthcheck_api

from db import init_db
from auth import register_auth_routers
>>>>>>>>> Temporary merge branch 2


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


def create_app():
    app = FastAPI(debug=True, lifespan=lifespan)

    register_auth_routers(app)
    app.include_router(healthcheck_api.router)
    app.include_router(events_api.router)
    app.include_router(localization_api.router)

    return app


app = create_app()
