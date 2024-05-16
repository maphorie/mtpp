all: style type lint test

lint:
	@echo $$'\e[33m========== pylint ==========\e[m'
	@pylint .

style:
	@echo $$'\e[33m========== flake8 ==========\e[m'
	@flake8 .

test:
	@echo $$'\e[33m========== pytest ==========\e[m'
	@pytest

type:
	@echo $$'\e[33m==========  mypy  ==========\e[m'
	@mypy .
