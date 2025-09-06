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
lint_sql file="./queries":
  # SQL Fix and lint
  ./scripts/sqlfluff_fix_and_lint.sh {{file}}

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

# Start PostgreSQL service
postgres_start:
    brew services start postgresql@14

# Stop PostgreSQL service
postgres_stop:
    brew services stop postgresql@14