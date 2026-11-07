.PHONY: install format lint test build run

install:
	uv sync --locked

format:
	uv run ruff format
	uv run ruff check --fix

lint:
	uv lock --check
	uv run ruff format --check
	uv run ruff check
	uv run mypy

test:
	uv run pytest

build:
	docker build -t app .

run:
	uv run app
