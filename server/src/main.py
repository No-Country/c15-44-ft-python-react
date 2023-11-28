from fastapi import FastAPI

from api import healthcheck
import events


def create_app():
    app = FastAPI(debug=True)

    app.include_router(healthcheck.router)
    app.include_router(events.router)

    return app


app = create_app()
