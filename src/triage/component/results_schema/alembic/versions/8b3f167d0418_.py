"""empty message

Revision ID: 8b3f167d0418
Revises:
Create Date: 2017-05-11 12:03:37.001446

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "8b3f167d0418"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SCHEMA results")
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "experiments",
        sa.Column("experiment_hash", sa.String(), nullable=False),
        sa.Column("config", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.PrimaryKeyConstraint("experiment_hash"),
        schema="results",
    )
    op.create_table(
        "model_groups",
        sa.Column("model_group_id", sa.Integer(), nullable=False),
        sa.Column("model_type", sa.Text(), nullable=True),
        sa.Column(
            "model_parameters", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("feature_list", sa.ARRAY(sa.Text()), nullable=True),
        sa.Column(
            "model_config", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.PrimaryKeyConstraint("model_group_id"),
        schema="results",
    )
    op.create_table(
        "models",
        sa.Column("model_id", sa.Integer(), nullable=False),
        sa.Column("model_group_id", sa.Integer(), nullable=True),
        sa.Column("model_hash", sa.String(), nullable=True),
        sa.Column("run_time", sa.DateTime(), nullable=True),
        sa.Column("batch_run_time", sa.DateTime(), nullable=True),
        sa.Column("model_type", sa.String(), nullable=True),
        sa.Column(
            "model_parameters", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("model_comment", sa.Text(), nullable=True),
        sa.Column("batch_comment", sa.Text(), nullable=True),
        sa.Column("config", sa.JSON(), nullable=True),
        sa.Column("experiment_hash", sa.String(), nullable=True),
        sa.Column("train_end_time", sa.DateTime(), nullable=True),
        sa.Column("test", sa.Boolean(), nullable=True),
        sa.Column("train_matrix_uuid", sa.Text(), nullable=True),
        sa.Column("train_label_window", sa.Interval(), nullable=True),
        sa.ForeignKeyConstraint(
            ["experiment_hash"], ["results.experiments.experiment_hash"]
        ),
        sa.ForeignKeyConstraint(
            ["model_group_id"], ["results.model_groups.model_group_id"]
        ),
        sa.PrimaryKeyConstraint("model_id"),
        schema="results",
    )
    op.create_index(
        op.f("ix_results_models_model_hash"),
        "models",
        ["model_hash"],
        unique=True,
        schema="results",
    )
    op.create_table(
        "evaluations",
        sa.Column("model_id", sa.Integer(), nullable=False),
        sa.Column("evaluation_start_time", sa.DateTime(), nullable=False),
        sa.Column("evaluation_end_time", sa.DateTime(), nullable=False),
        sa.Column("example_frequency", sa.Interval(), nullable=False),
        sa.Column("metric", sa.String(), nullable=False),
        sa.Column("parameter", sa.String(), nullable=False),
        sa.Column("value", sa.Numeric(), nullable=True),
        sa.Column("num_labeled_examples", sa.Integer(), nullable=True),
        sa.Column("num_labeled_above_threshold", sa.Integer(), nullable=True),
        sa.Column("num_positive_labels", sa.Integer(), nullable=True),
        sa.Column("sort_seed", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["model_id"], ["results.models.model_id"]),
        sa.PrimaryKeyConstraint(
            "model_id",
            "evaluation_start_time",
            "evaluation_end_time",
            "example_frequency",
            "metric",
            "parameter",
        ),
        schema="results",
    )
    op.create_table(
        "feature_importances",
        sa.Column("model_id", sa.Integer(), nullable=False),
        sa.Column("feature", sa.String(), nullable=False),
        sa.Column("feature_importance", sa.Numeric(), nullable=True),
        sa.Column("rank_abs", sa.Integer(), nullable=True),
        sa.Column("rank_pct", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(["model_id"], ["results.models.model_id"]),
        sa.PrimaryKeyConstraint("model_id", "feature"),
        schema="results",
    )
    op.create_table(
        "predictions",
        sa.Column("model_id", sa.Integer(), nullable=False),
        sa.Column("entity_id", sa.BigInteger(), nullable=False),
        sa.Column("as_of_date", sa.DateTime(), nullable=False),
        sa.Column("score", sa.Numeric(), nullable=True),
        sa.Column("label_value", sa.Integer(), nullable=True),
        sa.Column("rank_abs", sa.Integer(), nullable=True),
        sa.Column("rank_pct", sa.Float(), nullable=True),
        sa.Column("matrix_uuid", sa.Text(), nullable=True),
        sa.Column("test_label_window", sa.Interval(), nullable=True),
        sa.ForeignKeyConstraint(["model_id"], ["results.models.model_id"]),
        sa.PrimaryKeyConstraint("model_id", "entity_id", "as_of_date"),
        schema="results",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("predictions", schema="results")
    op.drop_table("feature_importances", schema="results")
    op.drop_table("evaluations", schema="results")
    op.drop_index(
        op.f("ix_results_models_model_hash"), table_name="models", schema="results"
    )
    op.drop_table("models", schema="results")
    op.drop_table("model_groups", schema="results")
    op.drop_table("experiments", schema="results")
    op.execute("DROP SCHEMA results")
    # ### end Alembic commands ###
