"""added data

Revision ID: ba9368a8219d
Revises: 7ea407408376
Create Date: 2021-06-28 19:17:14.646083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba9368a8219d'
down_revision = '7ea407408376'
branch_labels = None
depends_on = None


def upgrade():
    


    op.execute(records_table,
    [{'name': 'Ola', 'surname': 'Zmiiova', 'adress': 'Kyiv, Dryzby Narodov 26/1', 'email': 'zmiiova@i.ua', 'phone': '380506042357'}])


def downgrade():
    pass
