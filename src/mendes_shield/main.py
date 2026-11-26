"""Minimal application scaffold, intentionally without telemetry ingestion."""

from fastapi import FastAPI

app = FastAPI(
    title="Mendes Shield",
    version="0.0.1",
    description="Foundation-only API. No security detection or mitigation is implemented.",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Process liveness; no external dependencies exist in this phase."""
    return {"status": "ok"}


@app.get("/ready")
def ready() -> dict[str, str]:
    """Readiness for serving only these foundational API endpoints."""
    return {"status": "ready"}
