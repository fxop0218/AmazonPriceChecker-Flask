"""empty message

Revision ID: ecd148178661
Revises: a599ac6d280b
Create Date: 2022-11-11 22:41:04.772961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecd148178661'
down_revision = 'a599ac6d280b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=500), nullable=False),
    sa.Column('name', sa.String(length=252), nullable=False),
    sa.Column('first_price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('last_price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_product',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_product')
    op.drop_table('user_')
    op.drop_table('product')
    # ### end Alembic commands ###
