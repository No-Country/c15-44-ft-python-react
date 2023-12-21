from typing import Optional
import uuid
from fastapi import Depends, Request

from fastapi_users import UUIDIDMixin, BaseUserManager
from fastapi_users_db_sqlmodel import SQLModelUserDatabase
from .models import User
from .dependencies import get_user_db

from src.config import get_settings

settings = get_settings()


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.password_reset_secret
    verification_token_secret = settings.verification_secret

    # TODO: Add this and add validations to schemas
    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLModelUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
