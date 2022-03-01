init:
	pipenv install --dev

test:
	pipenv run pytest tests/
