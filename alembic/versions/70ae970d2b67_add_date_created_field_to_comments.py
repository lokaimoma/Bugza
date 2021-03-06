"""Add date created field to comments

Revision ID: 70ae970d2b67
Revises: 5ab29d80ef60
Create Date: 2022-02-13 17:13:08.529843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70ae970d2b67'
down_revision = '5ab29d80ef60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'date_created')
    # ### end Alembic commands ###
