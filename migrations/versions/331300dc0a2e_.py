"""empty message

Revision ID: 331300dc0a2e
Revises: 
Create Date: 2021-01-18 23:09:11.942605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '331300dc0a2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('bid', sa.Integer(), nullable=False),
    sa.Column('ISBN', sa.String(length=10), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('publisher', sa.String(length=100), nullable=False),
    sa.Column('book_cost', sa.String(length=100), nullable=False),
    sa.Column('pubDate', sa.DateTime(), nullable=False),
    sa.Column('bookImage', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('bid')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('age', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email', 'id', name='unique_component_commit')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('books')
    # ### end Alembic commands ###
