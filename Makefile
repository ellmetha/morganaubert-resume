.PHONY: init lint isort

init:
	pip install pipenv
	pipenv lock
	pipenv install --dev

lint:
	pipenv run flake8

isort:
	pipenv run isort --check-only --recursive --diff ma ma_project
