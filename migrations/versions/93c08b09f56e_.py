"""empty message

Revision ID: 93c08b09f56e
Revises: 36929bd315b9
Create Date: 2020-12-30 06:38:55.537448

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '93c08b09f56e'
down_revision = '36929bd315b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('id', table_name='my_market_day')
    op.drop_table('my_market_day')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_market_day',
    sa.Column('created', mysql.DATETIME(), nullable=False),
    sa.Column('updated', mysql.DATETIME(), nullable=False),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('day', mysql.DATETIME(), nullable=False),
    sa.Column('town_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['town_id'], ['town.id'], name='my_market_day_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'my_market_day', ['id'], unique=True)
    # ### end Alembic commands ###