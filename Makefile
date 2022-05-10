SHELL := /bin/bash

# Global stuff
DOCKER=docker
SOURCE_PATH := $(shell pwd)
WORKING_PATH=/opt
CONFIG="makefile.json"
UID := $(shell id -u)

# Docker config
DOCKER_RUN=$(DOCKER) run -u $(UID) -v $(SOURCE_PATH):$(WORKING_PATH) -w $(WORKING_PATH)

# Python config
PYTHON_CONTAINER=public.ecr.aws/replicant0wnz/build-python:latest
PYPI_USERNAME=__token__
PYPI_PASSWORD=$(token)

list:
	# List options of nothing specified
	grep '^[^#[:space:]].*:' Makefile

test:
	$(DOCKER_RUN) $(PYTHON_CONTAINER) python -m pytest tests

build:
	$(DOCKER_RUN) -e BUILD_VERSION=$(version) $(PYTHON_CONTAINER) python -m build

release_test:
	$(DOCKER_RUN) -e TWINE_USERNAME=$(PYPI_USERNAME) -e TWINE_PASSWORD=$(PYPI_PASSWORD) $(PYTHON_CONTAINER) python -m twine upload --verbose --repository testpypi dist/*

release:
	$(DOCKER_RUN) -e TWINE_USERNAME=$(PYPI_USERNAME) -e TWINE_PASSWORD=$(PYPI_PASSWORD) $(PYTHON_CONTAINER) python -m twine upload --verbose dist/*

clean:
	rm -rf dist .pytest_cache src/*egg-info

all: test build
