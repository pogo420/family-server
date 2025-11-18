rm -rf .venv

python3.12 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

gunicorn server_rest.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
