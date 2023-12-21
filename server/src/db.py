from functools import lru_cache
from sqlmodel import SQLModel, create_engine

from .config import get_settings

engine = create_engine(get_settings().database_url.get_secret_value())


def init_db():
    SQLModel.metadata.create_all(engine)


@lru_cache
def get_engine():
    return engine
