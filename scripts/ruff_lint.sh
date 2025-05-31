#!/bin/bash
#
# Run Ruff

echo
echo "-------- Ruff Lint --------"
echo

# Check
ruff check --fix

# Format .src and .tests
ruff format

echo
echo "--------------------------------"
echo