"""empty message

Revision ID: 8958c7cfecb4
Revises: 8091bf5877c3
Create Date: 2020-12-29 11:48:52.879059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8958c7cfecb4'
down_revision = '8091bf5877c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('market_day', sa.Column('created', sa.DateTime(), nullable=False))
    op.add_column('market_day', sa.Column('updated', sa.DateTime(), nullable=False))
    op.add_column('region', sa.Column('created', sa.DateTime(), nullable=False))
    op.add_column('region', sa.Column('updated', sa.DateTime(), nullable=False))
    op.add_column('town', sa.Column('created', sa.DateTime(), nullable=False))
    op.add_column('town', sa.Column('updated', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('town', 'updated')
    op.drop_column('town', 'created')
    op.drop_column('region', 'updated')
    op.drop_column('region', 'created')
    op.drop_column('market_day', 'updated')
    op.drop_column('market_day', 'created')
    # ### end Alembic commands ###
