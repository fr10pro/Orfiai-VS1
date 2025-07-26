#!/usr/bin/env bash
# (Optional) Debug installed packages:
# ./.venv/bin/pip list

# Launch via the venv’s Python interpreter
./.venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port $PORT
