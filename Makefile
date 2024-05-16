all: style type lint test

lint:
	@echo $$'\e[33m========== pylint ==========\e[m'
	@pylint --exit-zero .

style:
	@echo $$'\e[33m========== flake8 ==========\e[m'
	@flake8 --exit-zero .

test:
	@echo $$'\e[33m========== pytest ==========\e[m'
	@pytest

type:
	@echo $$'\e[33m==========  mypy  ==========\e[m'
	@mypy .
