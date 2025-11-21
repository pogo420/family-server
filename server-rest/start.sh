#!/bin/bash
cd /opt/server_rest

source venv/bin/activate

exec gunicorn server_rest.main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000
