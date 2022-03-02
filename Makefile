.PHONY: build

init:
	pipenv install --dev

build:
	pipenv run python -m build

test:
	pipenv run pytest tests/

deploy:
	TWINE_USERNAME=__token__ pipenv run python -m twine upload --repository pypi dist/*
