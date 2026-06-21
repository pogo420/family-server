#!/bin/bash
WORKERS=${WORKERS:-2}

exec gunicorn server_rest.main:app \
    --workers $WORKERS \
    --worker-class uvicorn.workers.UvicornWorker \
    --access-logfile - \
    --error-logfile -  \
    --bind 0.0.0.0:8000
