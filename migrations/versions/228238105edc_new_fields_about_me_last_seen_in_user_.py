"""new fields(about_me, last_seen) in user model

Revision ID: 228238105edc
Revises: e16feb58d262
Create Date: 2020-05-04 18:26:07.522965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '228238105edc'
down_revision = 'e16feb58d262'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_seen')
    op.drop_column('users', 'about_me')
    # ### end Alembic commands ###
