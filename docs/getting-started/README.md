# Getting Started

[Home](../../README.md) · [Architecture](../architecture/README.md) · [Roadmap](../roadmap.md) · [Contributing](../../CONTRIBUTING.md)

The only runnable component is the foundation FastAPI API. It exposes `/health` and `/ready` and the generated OpenAPI interface at `/docs`. It does not provide ingestion, anomaly detection, WAF integration, or mitigation.

## Local setup

Requirements: Python 3.12 or newer and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/ErikaMendes89/mendes-shield.git
cd mendes-shield
uv sync --dev
uv run uvicorn mendes_shield.main:app --reload
```

Open `http://127.0.0.1:8000/health`, `http://127.0.0.1:8000/ready`, or `http://127.0.0.1:8000/docs`.

## Docker

With Docker Compose installed:

```bash
docker compose up --build
```

The service binds to `127.0.0.1:8000` on the host.

## Development checks

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

These checks validate the foundation code; they do not measure security effectiveness or ML performance. See [CONTRIBUTING.md](../../CONTRIBUTING.md) for the current contribution status and privacy requirements.
