"""create records table

Revision ID: b2f1b6edfe06
Revises: 
Create Date: 2021-06-30 18:56:49.656145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2f1b6edfe06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'records',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('surname', sa.String(50), nullable=False),
        sa.Column('adress', sa.String(50), nullable=False),
        sa.Column('note', sa.String(50), nullable=False),
        sa.Column('tag', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('phone', sa.String(11), nullable=False),
        sa.Column('birthday', sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table('records')
