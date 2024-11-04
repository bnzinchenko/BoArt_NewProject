"""empty message

Revision ID: 886ae51d0957
Revises: 40547f81acf3
Create Date: 2024-11-04 15:37:10.494837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '886ae51d0957'
down_revision = '40547f81acf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('login', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('date', sa.DateTime(), nullable=True))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.drop_column('date')
        batch_op.drop_column('login')
        batch_op.drop_column('name')
        batch_op.drop_column('status')

    # ### end Alembic commands ###
