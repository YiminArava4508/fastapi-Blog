"""create posts table

Revision ID: 404ba273d5c0
Revises: 
Create Date: 2023-05-14 21:35:15.493553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '404ba273d5c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                            sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
