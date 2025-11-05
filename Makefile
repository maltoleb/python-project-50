install:
	uv sync
	
run:
	uv run gendiff

test:
	uv run pytest
	
build:
	uv build

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml
	
package-install:
	uv tool install dist/*.whl
	
lint:
	uv run ruff check

check: test lint

.PHONY: install test lint selfcheck check build



