#!/usr/bin/env just --justfile

# Load from '.env' file
set dotenv-load

# List available commands
help:
    @just --justfile {{justfile()}} --list --unsorted

# PyLint
lint:
  # Python PyLint lint from ./src and ./tests
  ./scripts/pylint_lint.sh

# SQLFluff
lint_sql file="./queries":
  # SQL Fix and lint
  ./scripts/sqlfluff_fix_and_lint.sh {{file}}

# Run Pytest
test:
  poetry run pytest

# Launch Jupyter Lab
jupy:
  poetry run jupyter lab