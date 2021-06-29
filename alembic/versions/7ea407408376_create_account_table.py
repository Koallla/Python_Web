"""create account table

Revision ID: 7ea407408376
Revises: 
Create Date: 2021-06-28 19:04:38.214179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ea407408376'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    records_table = op.create_table(
        'records',
        sa.Column('id', sa.Integer, sa.Sequence('user_id_seq'), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('surname', sa.String(50), nullable=False),
        sa.Column('adress', sa.String(200), nullable=False),
        sa.Column('note', sa.String(500)),
        sa.Column('tag', sa.String(200)),
        sa.Column('email', sa.String(200), nullable=False),
        sa.Column('phone', sa.String(300), nullable=False),
        
    )

    op.bulk_insert(records_table,
    [{'name': 'Mihail', 'surname': 'Zmiiov', 'adress': 'Kyiv, Dryzby Narodov 26/1', 'email': 'z@i.ua', 'phone': '380953128882'}])

def downgrade():
    pass
