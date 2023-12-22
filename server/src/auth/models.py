from fastapi_users_db_sqlmodel import SQLModelBaseUserDB
from sqlmodel import SQLModel
import typing
from pydantic import EmailStr


class User(SQLModelBaseUserDB, table=True):
    email: typing.Annotated[str,EmailStr]
