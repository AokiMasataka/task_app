# ===== Build Stage =====
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential pkg-config libssl-dev&& \
    rm -rf /var/lib/apt/lists/*

COPY ./pyproject.toml ./uv.lock /app/
RUN uv sync --no-dev

# ===== Runtime Stage =====
FROM python:3.12-slim

WORKDIR /app

ENV TZ=Asia/Tokyo

COPY --from=builder /app/.venv /app/.venv
COPY ./app /app

CMD ["/app/.venv/bin/python", "/app/main.py"]