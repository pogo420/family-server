FROM python:3.12-slim

RUN pip install poetry

WORKDIR /server-rest-api

# Copying poetry files
COPY pyproject.toml poetry.lock /server-rest-api
RUN poetry install --only main --no-root --no-directory

# Copying unicorn config
COPY gunicorn.conf.py /server-rest-api

# Copy source code
COPY server_rest_api/ /server-rest-api/server_rest_api
RUN poetry install --only main

# Exposing port
EXPOSE 5001

# App entry point
CMD ["poetry", "run", "gunicorn"]
