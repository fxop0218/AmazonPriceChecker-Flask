"""empty message

Revision ID: 51070bf7c4a8
Revises: 4b6703cc3377
Create Date: 2022-11-11 20:11:21.030562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51070bf7c4a8'
down_revision = '4b6703cc3377'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=500), nullable=False),
    sa.Column('name', sa.String(length=252), nullable=False),
    sa.Column('first_price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('last_price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('password', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    op.drop_table('products')
    # ### end Alembic commands ###
