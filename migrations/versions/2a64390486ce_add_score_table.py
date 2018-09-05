"""Add score table

Revision ID: 2a64390486ce
Revises: 
Create Date: 2018-09-05 11:06:24.106652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a64390486ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('score',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=90), nullable=True),
    sa.Column('falg_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_score_falg_count'), 'score', ['falg_count'], unique=False)
    op.create_index(op.f('ix_score_username'), 'score', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_score_username'), table_name='score')
    op.drop_index(op.f('ix_score_falg_count'), table_name='score')
    op.drop_table('score')
    # ### end Alembic commands ###
