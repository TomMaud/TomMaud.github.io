"""Adding User Table

Revision ID: 526275b4f528
Revises: a73ecc82439e
Create Date: 2024-10-25 20:15:32.208912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '526275b4f528'
down_revision = 'a73ecc82439e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mfaenabled', sa.Boolean(), nullable=False))
        batch_op.drop_column('mfaenables')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mfaenables', sa.BOOLEAN(), nullable=False))
        batch_op.drop_column('mfaenabled')

    # ### end Alembic commands ###