"""empty message

Revision ID: 0bf52ecae1a2
Revises: 90222c9a3de6
Create Date: 2022-11-12 16:14:48.554696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bf52ecae1a2'
down_revision = '90222c9a3de6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user_', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_', type_='unique')
    # ### end Alembic commands ###
