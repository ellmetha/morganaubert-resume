PROJECT_PACKAGE := ma

.PHONY: devserver qa lint lint_python isort isort_python tests tests_python spec spec_python


init:
	pipenv install --dev --three
	npm install


# DEVELOPMENT
# ~~~~~~~~~~~
# The following rules can be used during development in order to launch development server, generate
# locales, etc.
# --------------------------------------------------------------------------------------------------

s: server
server:
	FLASK_APP=wsgi.py FLASK_ENV=development pipenv run flask run

c: console
console:
	FLASK_APP=wsgi.py FLASK_ENV=development pipenv run flask shell


# QUALITY ASSURANCE
# ~~~~~~~~~~~~~~~~~
# The following rules can be used to check code quality, import sorting, etc.
# --------------------------------------------------------------------------------------------------

qa: lint isort

# Code quality checks (eg. flake8, etc).
lint: lint_python lint_js
lint_python:
	pipenv run flake8
lint_js:
	npm run lint

# Import sort checks.
isort: isort_python
isort_python:
	pipenv run isort --check-only --recursive --diff $(PROJECT_PACKAGE)


# TESTING
# ~~~~~~~
# The following rules can be used to trigger tests execution and produce coverage reports.
# --------------------------------------------------------------------------------------------------

# Just runs all the tests!
t: tests
tests: tests_js
tests_js:
	npm test

# Collects code coverage data.
coverage: coverage_python coverage_js
coverage_python:
	pipenv run py.test --cov-report term-missing --cov $(PROJECT_PACKAGE)
coverage_js:
	npm test

# Run the tests in "spec" mode.
spec: spec_python
spec_python:
	pipenv run py.test --spec -p no:sugar
