all: format lint test type

format:
	@echo $$'\e[33m========== format ==========\e[m'
	@poetry run ruff format --line-length 127

lint:
	@echo $$'\e[33m==========  lint  ==========\e[m'
	@poetry run ruff check --exit-zero

test:
	@echo $$'\e[33m==========  test  ==========\e[m'
	@poetry run pytest

type:
	@echo $$'\e[33m==========  type  ==========\e[m'
	@poetry run mypy --ignore-missing-imports .
