#!/usr/bin/env just --justfile

# Load from '.env' file
set dotenv-load

# List available commands
help:
    @just --justfile {{justfile()}} --list --unsorted

# Ruff
lint:
  # Python ruff lint
  ./scripts/ruff_lint.sh

# SQLFluff
lint_sql file="./queries" dialect="postgres":
  # SQL Fix and lint
  ./scripts/sqlfluff_fix_and_lint.sh {{file}} {{dialect}}

# Run pre-commit
pre:
  pre-commit run --all-files

# Run Pytest
test:
  uv run pytest

# Launch Jupyter Lab
jupy:
  uv run jupyter lab

# Login with gcloud
gcloud_login:
    gcloud auth login
    gcloud config set project $PROJECT_ID
    gcloud auth application-default login

# ------------------ StackOverflow Answer Classification use Case ------------------
# Execute the Raw Data Metaflow pipeline. Available commands: 'run', 'show'
answer_raw_data command:
  uv run python -m src.stackoverflow.pipelines.data.answer_score_raw_data_flow {{command}}
# ----------------------------------------------------------------------------------