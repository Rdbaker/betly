"""empty message

Revision ID: 8b9f5b081137
Revises: 19cabd29fb71
Create Date: 2016-08-27 17:29:41.137566

"""

# revision identifiers, used by Alembic.
revision = '8b9f5b081137'
down_revision = '19cabd29fb71'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bet',
    sa.Column('guid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('organizer', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('url_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('bet_type', sa.Text(), nullable=True),
    sa.Column('options', sa.Text(), nullable=True),
    sa.Column('amount', sa.Float(precision=2), nullable=True),
    sa.Column('bet_status', sa.Text(), nullable=True),
    sa.Column('outcome_option_value', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['organizer'], ['user.id'], ),
    sa.PrimaryKeyConstraint('guid')
    )
    op.create_table('user_bet',
    sa.Column('user_guid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('bet_guid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['bet_guid'], ['bet.guid'], ),
    sa.ForeignKeyConstraint(['user_guid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_guid', 'bet_guid')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_bet')
    op.drop_table('bet')
    ### end Alembic commands ###
