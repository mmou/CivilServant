"""add user table

Revision ID: 66a893890997
Revises: e06fa0a86214
Create Date: 2016-06-28 14:52:01.114605

"""

# revision identifiers, used by Alembic.
revision = '66a893890997'
down_revision = 'e06fa0a86214'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_development():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', sa.String(length=32), autoincrement=False, nullable=False),
    sa.Column('id', sa.String(length=32), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('first_seen', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('user_data', mysql.MEDIUMTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # removed to fix merge conflict
    #op.add_column('posts', sa.Column('created_at', sa.DateTime(), nullable=True))
#    op.drop_index('posts_ibfk_1', table_name='posts')
    op.add_column('subreddits', sa.Column('created_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade_development():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subreddits', 'created_at')
#    op.create_index('posts_ibfk_1', 'posts', ['subreddit_id'], unique=False)
    # removed to fix merge conflict
    #op.drop_column('posts', 'created_at')
    op.drop_table('users')
    ### end Alembic commands ###


def upgrade_test():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', sa.String(length=32), autoincrement=False, nullable=False),
    sa.Column('id', sa.String(length=32), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('first_seen', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('user_data', mysql.MEDIUMTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # removed to fix merge conflict
    #op.add_column('posts', sa.Column('created_at', sa.DateTime(), nullable=True))
#    op.drop_index('posts_ibfk_1', table_name='posts')
    op.add_column('subreddits', sa.Column('created_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade_test():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subreddits', 'created_at')
#    op.create_index('posts_ibfk_1', 'posts', ['subreddit_id'], unique=False)
    # removed to fix merge conflict
    #op.drop_column('posts', 'created_at')
    op.drop_table('users')
    ### end Alembic commands ###


def upgrade_production():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', sa.String(length=32), autoincrement=False, nullable=False),
    sa.Column('id', sa.String(length=32), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('first_seen', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('user_data', mysql.MEDIUMTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # removed to fix merge conflict
    #op.add_column('posts', sa.Column('created_at', sa.DateTime(), nullable=True))
#    op.drop_index('posts_ibfk_1', table_name='posts')
    op.add_column('subreddits', sa.Column('created_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade_production():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subreddits', 'created_at')
#    op.create_index('posts_ibfk_1', 'posts', ['subreddit_id'], unique=False)
    # removed to fix merge conflict
    #op.drop_column('posts', 'created_at')
    op.drop_table('users')
    ### end Alembic commands ###

