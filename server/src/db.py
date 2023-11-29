from sqlmodel import SQLModel, create_engine

from config import get_settings

engine = create_engine(get_settings().database_url)


def init_db():
    SQLModel.metadata.create_all(engine)
