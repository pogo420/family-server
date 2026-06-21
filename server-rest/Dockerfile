# ==================================================
# Builder
# ==================================================
FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /build

RUN pip install --no-cache-dir poetry

# Dependency layer
COPY pyproject.toml poetry.lock ./

RUN poetry install --only main --no-root

# Application source
COPY . .

# Build wheel
RUN poetry build

# ==================================================
# Runtime
# ==================================================
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Non-root user
RUN useradd --create-home --shell /bin/bash appuser

# Install application wheel
COPY --from=builder /build/dist/*.whl /tmp/

RUN pip install --no-cache-dir /tmp/*.whl && \
    rm -rf /tmp/*.whl

# Startup script
COPY --from=builder /build/start.sh /start.sh

RUN chmod +x /start.sh

USER appuser

EXPOSE 8000

CMD ["/start.sh"]
