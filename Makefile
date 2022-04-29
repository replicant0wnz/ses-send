SHELL := /bin/bash

# Global stuff
DOCKER=docker
SOURCE_PATH := $(shell pwd)
WORKING_PATH=/opt
CONFIG="makefile.json"
UID := $(shell id -u)

# jq config
JQ_CONTAINER=imega/jq
JQ=$(DOCKER) run -i $(JQ_CONTAINER) -c

# Docker config
DOCKER_RUN=$(DOCKER) run -u $(UID) -v $(SOURCE_PATH):$(WORKING_PATH) -w $(WORKING_PATH)

# Python config
PYTHON_CONTAINER=build-python:local
PYPI_USERNAME=__token__
PYPI_PASSWORD=$(token)

## Github config
#GH_CONTAINER=ghcr.io/supportpal/github-gh-cli
#GH=$(DOCKER) run -e GH_TOKEN=$$GH_TOKEN -v $(SOURCE_PATH):$(WORKING_PATH) -w $(WORKING_PATH) $(GH_CONTAINER)

# AWS config
AWS_CONTAINER=amazon/aws-cli
AWS_WORKING_PATH=/aws
AWS=$(DOCKER) run -e AWS_SECRET_ACCESS_KEY=$$AWS_SECRET_ACCESS_KEY -e AWS_ACCESS_KEY_ID=$$AWS_ACCESS_KEY_ID 

## Items from $(CONFIG)
#S3_BUCKET := $(shell cat $(CONFIG) | $(JQ) .aws.s3.destination)
#S3_REGION := $(shell cat $(CONFIG) | $(JQ) .aws.s3.region)
#DISTRIBUTION_ID := $(shell cat $(CONFIG) | $(JQ) .aws.cloudfront.distribution_id)
#INVALIDATION_PATH := $(shell cat $(CONFIG) | $(JQ) .aws.cloudfront.invalidation_path) 

test:
	$(DOCKER_RUN) $(PYTHON_CONTAINER) python -m pytest tests

build:
	$(DOCKER_RUN) -e BUILD_VERSION=$(version) $(PYTHON_CONTAINER) python -m build

release:
	$(GH) gh release create $(version) dist.tar.gz --generate-notes

deploy:
	$(DOCKER_RUN) -e TWINE_USERNAME=$(PYPI_USERNAME) -e TWINE_PASSWORD=$(PYPI_PASSWORD) $(PYTHON_CONTAINER) python -m twine upload --repository testpypi dist/*

clean:
	rm -rf dist .pytest_cache

all: init build package
