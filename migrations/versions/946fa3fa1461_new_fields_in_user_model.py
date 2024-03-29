"""new fields in user model

Revision ID: 946fa3fa1461
Revises: 1f234eb6f749
Create Date: 2019-09-15 01:01:11.658718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '946fa3fa1461'
down_revision = '1f234eb6f749'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
