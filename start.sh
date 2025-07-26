#!/usr/bin/env bash
# (Optional debug) Show installed packages:
# ./.venv/bin/pip list

# Run uvicorn via the venv’s Python
./.venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port $PORT
