"""add_experiment_runs

Revision ID: cfd5c3386014
Revises: 50e1f1bc2cac
Create Date: 2019-03-15 12:08:51.995548

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import datetime

# revision identifiers, used by Alembic.
revision = 'cfd5c3386014'
down_revision = '50e1f1bc2cac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('experiment_runs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('start_method', sa.String(), nullable=True),
    sa.Column('git_hash', sa.String(), nullable=True),
    sa.Column('triage_version', sa.String(), nullable=True),
    sa.Column('experiment_hash', sa.String(), nullable=True),
    sa.Column('platform', sa.Text(), nullable=True),
    sa.Column('os_user', sa.Text(), nullable=True),
    sa.Column('working_directory', sa.Text(), nullable=True),
    sa.Column('ec2_instance_type', sa.Text(), nullable=True),
    sa.Column('log_location', sa.Text(), nullable=True),
    sa.Column('experiment_class_path', sa.Text(), nullable=True),
    sa.Column('experiment_kwargs', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('installed_libraries', sa.ARRAY(sa.Text()), nullable=True),
    sa.Column('matrix_building_started', sa.DateTime(), nullable=True),
    sa.Column('matrices_made', sa.Integer(), nullable=False, default=0),
    sa.Column('matrices_skipped', sa.Integer(), nullable=False, default=0),
    sa.Column('matrices_errored', sa.Integer(), nullable=False, default=0),
    sa.Column('model_building_started', sa.DateTime(), nullable=True),
    sa.Column('models_made', sa.Integer(), nullable=False, default=0),
    sa.Column('models_skipped', sa.Integer(), nullable=False, default=0),
    sa.Column('models_errored', sa.Integer(), nullable=False, default=0),
    sa.Column('last_updated_time', sa.DateTime(), nullable=True, onupdate=datetime.datetime.now),
    sa.Column('current_status', sa.Enum('started', 'completed', 'failed', name='experimentrunstatus'), nullable=True),
    sa.Column('stacktrace', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['experiment_hash'], ['model_metadata.experiments.experiment_hash'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='model_metadata'
    )

    op.add_column('experiments', sa.Column('time_splits', sa.Integer(), nullable=True), schema='model_metadata')
    op.add_column('experiments', sa.Column('as_of_times', sa.Integer(), nullable=True), schema='model_metadata')
    op.add_column('experiments', sa.Column('feature_blocks', sa.Integer(), nullable=True), schema='model_metadata')
    op.add_column('experiments', sa.Column('total_features', sa.Integer(), nullable=True), schema='model_metadata')
    op.add_column('experiments', sa.Column('feature_group_combinations', sa.Integer(), nullable=True), schema='model_metadata')
    op.add_column('experiments', sa.Column('matrices_needed', sa.Integer(), nullable=True), schema='model_metadata')
    op.add_column('experiments', sa.Column('grid_size', sa.Integer(), nullable=True), schema='model_metadata')
    op.add_column('experiments', sa.Column('models_needed', sa.Integer(), nullable=True), schema='model_metadata')

    op.add_column('matrices', sa.Column('feature_dictionary', postgresql.JSONB(astext_type=sa.Text()), nullable=True), schema='model_metadata')
    # ### end Alembic commands ###


def downgrade():
    op.drop_column('matrices', 'feature_dictionary', schema='model_metadata')

    op.drop_column('experiments', 'models_needed', schema='model_metadata')
    op.drop_column('experiments', 'grid_size', schema='model_metadata')
    op.drop_column('experiments', 'matrices_needed', schema='model_metadata')
    op.drop_column('experiments', 'feature_group_combinations', schema='model_metadata')
    op.drop_column('experiments', 'total_features', schema='model_metadata')
    op.drop_column('experiments', 'feature_blocks', schema='model_metadata')
    op.drop_column('experiments', 'as_of_times', schema='model_metadata')
    op.drop_column('experiments', 'time_splits', schema='model_metadata')
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('experiment_runs', schema='model_metadata')
    # ### end Alembic commands ###
