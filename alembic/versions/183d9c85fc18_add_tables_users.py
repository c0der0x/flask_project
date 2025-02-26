"""add tables Users

Revision ID: 183d9c85fc18
Revises: 
Create Date: 2025-02-26 07:40:09.354234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183d9c85fc18'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "user",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("username", sa.String),
            sa.Column("password", sa.String))


def downgrade():
    op.drop_table("user")
