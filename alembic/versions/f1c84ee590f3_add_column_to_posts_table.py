"""add column to posts table

Revision ID: f1c84ee590f3
Revises: 278fdd6195fd
Create Date: 2023-05-18 19:48:44.345588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1c84ee590f3'
down_revision = '278fdd6195fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
