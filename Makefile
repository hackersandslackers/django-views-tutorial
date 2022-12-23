PROJECT_NAME := $(shell basename $CURDIR)
VIRTUAL_ENV := $(CURDIR)/.venv
LOCAL_PYTHON := $(VIRTUAL_ENV)/bin/python3

define HELP
Manage $(PROJECT_NAME). Usage:

make run        - Run $(PROJECT_NAME).
make install    - Install Python dependencies in a virtual environment.
make update     - Update pip dependencies via Python Poetry.
make format     - Format code with Python's `Black` library.
make clean      - Remove cached files and lock files.
endef
export HELP

.PHONY: run deploy update format clean help


all help:
	@echo "$$HELP"

env: $(VIRTUAL_ENV)


$(VIRTUAL_ENV):
	if [ ! -d $(VIRTUAL_ENV) ]; then \
		echo "Creating Python virtual env in \`${VIRTUAL_ENV}\`"; \
		python3 -m venv $(VIRTUAL_ENV); \
	fi


.PHONY: install
install: env
	$(LOCAL_PYTHON) -m pip install --upgrade pip setuptools wheel && \
	$(LOCAL_PYTHON) -m pip install -r requirements.txt && \
	echo Installed dependencies in \`${VIRTUAL_ENV}\`;


.PHONY: run
run: env
	$(shell . ./deploy.sh)


.PHONY: update
update: env
	$(LOCAL_PYTHON) -m pip install --upgrade pip setuptools wheel && \
	poetry update && \
	poetry export -f requirements.txt --output requirements.txt --without-hashes && \
	echo Installed dependencies in \`${VIRTUAL_ENV}\`;


.PHONY: format
format: env
	$(LOCAL_PYTHON) -m isort --multi-line=3 .
	$(LOCAL_PYTHON) -m black .


.PHONY: lint
lint: env
	$(LOCAL_PYTHON) -m flake8 . --count \
			--select=E9,F63,F7,F82 \
			--exclude .git,.github,__pycache__,.pytest_cache,.venv,logs,creds,.venv,docs,logs,.reports \
			--show-source \
			--statistics


.PHONY: clean
clean:
	find . -name 'poetry.lock' -delete && \
	find . -name '.coverage' -delete && \
	find . -wholename '**/*.pyc' -delete && \
	find . -type d -wholename '__pycache__' -exec rm -rf {} + && \
	find . -type d -wholename '.venv' -exec rm -rf {} + && \
	find . -type d -wholename '.pytest_cache' -exec rm -rf {} + && \
	find . -type d -wholename '**/.pytest_cache' -exec rm -rf {} + && \
	find . -type d -wholename './logs/*' -exec rm -rf {} + && \
	find . -type d -wholename './.reports/*' -exec rm -rf {} +