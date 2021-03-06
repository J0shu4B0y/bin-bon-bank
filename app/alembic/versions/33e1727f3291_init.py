"""Init

Revision ID: 33e1727f3291
Revises: 
Create Date: 2020-11-27 10:40:57.178504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33e1727f3291'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('currency', sa.String(), autoincrement=False, nullable=True),
    sa.Column('amount', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('client_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), autoincrement=False, nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id')
    )
    op.create_index(op.f('ix_account_version_amount'), 'account_version', ['amount'], unique=False)
    op.create_index(op.f('ix_account_version_currency'), 'account_version', ['currency'], unique=False)
    op.create_index(op.f('ix_account_version_end_transaction_id'), 'account_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_account_version_id'), 'account_version', ['id'], unique=False)
    op.create_index(op.f('ix_account_version_operation_type'), 'account_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_account_version_transaction_id'), 'account_version', ['transaction_id'], unique=False)
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_email'), 'client', ['email'], unique=True)
    op.create_index(op.f('ix_client_full_name'), 'client', ['full_name'], unique=False)
    op.create_index(op.f('ix_client_id'), 'client', ['id'], unique=False)
    op.create_table('transaction',
    sa.Column('issued_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('remote_addr', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_account_amount'), 'account', ['amount'], unique=False)
    op.create_index(op.f('ix_account_currency'), 'account', ['currency'], unique=False)
    op.create_index(op.f('ix_account_id'), 'account', ['id'], unique=False)
    op.create_table('account_transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('create', 'deposit', 'withdraw', name='accounttransactiontype'), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_account_transaction_amount'), 'account_transaction', ['amount'], unique=False)
    op.create_index(op.f('ix_account_transaction_id'), 'account_transaction', ['id'], unique=False)
    op.create_index(op.f('ix_account_transaction_type'), 'account_transaction', ['type'], unique=False)
    op.create_index(op.f('ix_account_transaction_uuid'), 'account_transaction', ['uuid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_account_transaction_uuid'), table_name='account_transaction')
    op.drop_index(op.f('ix_account_transaction_type'), table_name='account_transaction')
    op.drop_index(op.f('ix_account_transaction_id'), table_name='account_transaction')
    op.drop_index(op.f('ix_account_transaction_amount'), table_name='account_transaction')
    op.drop_table('account_transaction')
    op.drop_index(op.f('ix_account_id'), table_name='account')
    op.drop_index(op.f('ix_account_currency'), table_name='account')
    op.drop_index(op.f('ix_account_amount'), table_name='account')
    op.drop_table('account')
    op.drop_table('transaction')
    op.drop_index(op.f('ix_client_id'), table_name='client')
    op.drop_index(op.f('ix_client_full_name'), table_name='client')
    op.drop_index(op.f('ix_client_email'), table_name='client')
    op.drop_table('client')
    op.drop_index(op.f('ix_account_version_transaction_id'), table_name='account_version')
    op.drop_index(op.f('ix_account_version_operation_type'), table_name='account_version')
    op.drop_index(op.f('ix_account_version_id'), table_name='account_version')
    op.drop_index(op.f('ix_account_version_end_transaction_id'), table_name='account_version')
    op.drop_index(op.f('ix_account_version_currency'), table_name='account_version')
    op.drop_index(op.f('ix_account_version_amount'), table_name='account_version')
    op.drop_table('account_version')
    # ### end Alembic commands ###
