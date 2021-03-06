"""empty message

Revision ID: b7589efa02a0
Revises: b5658f866fa4
Create Date: 2021-06-23 02:08:51.578032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7589efa02a0'
down_revision = 'b5658f866fa4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'genres',
        sa.Column(
            'id',
            sa.INTEGER(),
            server_default=sa.text('nextval(\'"Genre_id_seq"\'::regclass)'),
            autoincrement=True,
            nullable=False
        ),
        sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='Genre_pkey'),
        sa.UniqueConstraint('name', name='Genre_name_key')
    )
    # ### end Alembic commands ###
