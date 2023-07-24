"""added more columns

Revision ID: c5708e6346cd
Revises: 3df2c881bc84
Create Date: 2023-07-23 21:28:28.616429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5708e6346cd'
down_revision = '3df2c881bc84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weight', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('height', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.drop_column('height')
        batch_op.drop_column('weight')

    # ### end Alembic commands ###
