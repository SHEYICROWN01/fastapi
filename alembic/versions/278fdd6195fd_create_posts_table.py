"""create posts table

Revision ID: 278fdd6195fd
Revises: 
Create Date: 2023-05-18 19:37:54.729162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '278fdd6195fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('post')
    pass
