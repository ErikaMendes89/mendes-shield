.PHONY: install test lint typecheck serve check
install:
	uv sync --dev
serve:
	uv run uvicorn mendes_shield.main:app --reload
test:
	uv run pytest
lint:
	uv run ruff check .
typecheck:
	uv run mypy src
check: lint typecheck test
