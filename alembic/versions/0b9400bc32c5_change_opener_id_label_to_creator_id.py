"""Change opener_id label to creator_id

Revision ID: 0b9400bc32c5
Revises: cec07567f068
Create Date: 2022-02-01 12:31:25.551288

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0b9400bc32c5'
down_revision = 'cec07567f068'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('creator_id', sa.BIGINT(), nullable=True))
    op.drop_constraint('tickets_ibfk_1', 'tickets', type_='foreignkey')
    op.create_foreign_key(None, 'tickets', 'users', ['creator_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('tickets', 'opener_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('opener_id', mysql.BIGINT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'tickets', type_='foreignkey')
    op.create_foreign_key('tickets_ibfk_1', 'tickets', 'users', ['opener_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('tickets', 'creator_id')
    # ### end Alembic commands ###
