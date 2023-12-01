from fastapi_users_db_sqlmodel import SQLModelBaseUserDB
from sqlmodel import SQLModel


class User(SQLModelBaseUserDB, table=True):
    pass
