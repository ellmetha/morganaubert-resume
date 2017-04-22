.PHONY: init

init:
	pip install pipenv
	pipenv lock
	pipenv install --dev
