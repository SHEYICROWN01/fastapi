"""add user table

Revision ID: 41ab7c8bda6e
Revises: f1c84ee590f3
Create Date: 2023-05-18 19:56:57.808610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41ab7c8bda6e'
down_revision = 'f1c84ee590f3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),nullable=False),
                              sa.PrimaryKeyConstraint('id'),
                              sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
