from fastapi import FastAPI

from api import healthcheck


def create_app():
    app = FastAPI()

    app.include_router(healthcheck.router)

    return app


app = create_app()
