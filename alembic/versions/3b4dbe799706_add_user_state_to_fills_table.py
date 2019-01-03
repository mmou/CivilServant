"""add user_state to fills table

Revision ID: 3b4dbe799706
Revises: cd494c3a75aa
Create Date: 2019-01-02 16:14:57.307986

"""

# revision identifiers, used by Alembic.
revision = '3b4dbe799706'
down_revision = 'cd494c3a75aa'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_development():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('twitter_fills', sa.Column('user_state', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade_development():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('twitter_fills', 'user_state')
    # ### end Alembic commands ###


def upgrade_test():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('twitter_fills', sa.Column('user_state', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade_test():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('twitter_fills', 'user_state')
    # ### end Alembic commands ###


def upgrade_production():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('twitter_fills', sa.Column('user_state', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade_production():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('twitter_fills', 'user_state')
    # ### end Alembic commands ###

