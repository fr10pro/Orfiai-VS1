#!/usr/bin/env bash
# Use the virtual environment python executable explicitly
./.venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port $PORT
