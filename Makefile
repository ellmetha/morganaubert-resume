PROJECT_PACKAGE := main


## Setup and initialize the project for development.
init:
	@printf "${YELLOW}---------------- Initialization ---${RESET} ${GREEN}Environment settings${RESET}\n\n"

	rsync --ignore-existing .env.json.example .env.json

	@printf "\n\n${YELLOW}---------------- Initialization ---${RESET} ${GREEN}Python dependencies${RESET}\n\n"

	poetry env use 3.8
	poetry install

	@printf "\n\n${YELLOW}---------------- Initialization ---${RESET} ${GREEN}Node.js dependencies${RESET}\n\n"

	npm install

	@printf "\n\n${YELLOW}---------------- Initialization ---${RESET} ${GREEN}Initial assets build${RESET}\n\n"

	npm run gulp -- build

	@printf "\n\n${YELLOW}---------------- Done.${RESET}\n\n"


# DEVELOPMENT
# ~~~~~~~~~~~
# The following rules can be used during development in order to launch development server, generate
# locales, etc.
# --------------------------------------------------------------------------------------------------

.PHONY: s server
## Alias of "server".
s: server
## Launch a development server.
server:
	FLASK_APP=wsgi.py FLASK_ENV=development poetry run flask run

.PHONY: c console
## Alias of "console".
c: console
## Launch a development console.
console:
	FLASK_APP=wsgi.py FLASK_ENV=development poetry run flask shell


# QUALITY ASSURANCE
# ~~~~~~~~~~~~~~~~~
# The following rules can be used to check code quality, import sorting, etc.
# --------------------------------------------------------------------------------------------------

.PHONY: qa
## Trigger all quality assurance checks.
qa: lint isort

.PHONY: lint lint_python lint_js
## Trigger code quality checks (flake8, eslint).
lint: lint_python lint_js
## Trigger Python code quality checks (flake8).
lint_python:
	poetry run flake8
## Trigger Javascript code quality checks (eslint).
lint_js:
	npm run lint

.PHONY: isort isort_python
## Check Python imports sorting.
isort: isort_python
## Check Python imports sorting.
isort_python:
	poetry run isort --check-only --recursive --diff $(PROJECT_PACKAGE)


# TESTING
# ~~~~~~~
# The following rules can be used to trigger tests execution and produce coverage reports.
# --------------------------------------------------------------------------------------------------

.PHONY: t tests tests_js
## Alias of "tests".
t: tests
## Run all the test suites.
tests: tests_js
## Run the Javascript test suite.
tests_js:
	npm test

.PHONY: coverage coverage_js
## Collects code coverage data.
coverage: coverage_python coverage_js
## Collects code coverage data for the Javascript codebase.
coverage_js:
	npm test


# MAKEFILE HELPERS
# ~~~~~~~~~~~~~~~~
# The following rules can be used to list available commands and to display help messages.
# --------------------------------------------------------------------------------------------------

# COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

.PHONY: help
## Print Makefile help.
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<action>${RESET}'
	@echo ''
	@echo 'Actions:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)-30s${RESET}\t${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST) | sort -t'|' -sk1,1
