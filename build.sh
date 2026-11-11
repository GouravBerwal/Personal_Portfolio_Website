#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

# Determine python command
if command -v python3 &>/dev/null; then
    PY_CMD="python3"
else
    PY_CMD="python"
fi

echo "==> Installing Python dependencies..."
pip install -r requirements.txt

echo "==> Collecting static assets..."
$PY_CMD manage.py collectstatic --no-input

echo "==> Applying database migrations..."
$PY_CMD manage.py migrate

echo "==> Seeding portfolio data..."
$PY_CMD manage.py seed_portfolio

echo "==> Build finished successfully!"
