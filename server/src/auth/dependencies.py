from fastapi import Depends
from fastapi_users_db_sqlmodel import SQLModelUserDatabase
from sqlalchemy import Engine
from sqlmodel import Session

from src.db import get_engine

from .models import User


async def get_user_db(engine: Engine = Depends(get_engine)):
    with Session(engine) as session:
        yield SQLModelUserDatabase(session, User)
