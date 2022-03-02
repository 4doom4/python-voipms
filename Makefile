.PHONY: build

init:
	pipenv install --dev

build:
	pipenv run python -m build

test:
	pipenv run pytest tests/
