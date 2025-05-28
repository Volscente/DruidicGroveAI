#!/bin/bash
#
# Run Ruff

echo
echo "-------- Ruff Lint --------"
echo

# Check
ruff check --fix

# Format
ruff format

echo
echo "--------------------------------"
echo