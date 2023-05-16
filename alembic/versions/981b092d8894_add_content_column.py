"""add content column

Revision ID: 981b092d8894
Revises: 404ba273d5c0
Create Date: 2023-05-15 20:15:48.911242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '981b092d8894'
down_revision = '404ba273d5c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

    pass


def downgrade() -> None:
    op.drop_column('posts', 'column')
    pass
