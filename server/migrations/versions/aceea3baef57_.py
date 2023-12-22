"""empty message

Revision ID: aceea3baef57
Revises: 46111f956fad, bec10c6ddfa8
Create Date: 2023-12-05 12:16:46.213209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'aceea3baef57'
down_revision: Union[str, None] = ('46111f956fad', 'bec10c6ddfa8')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
