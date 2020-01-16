# import config.
# You can change the default config with `make cnf="config_special.env" build`
#cnf ?= docker-files/config.env
#include $(cnf)
#export $(shell sed 's/=.*//' $(cnf))

# import deploy config
# You can change the default deploy config with `make cnf="deploy_special.env" release`
dpl ?= docker-files/deploy.env
include $(dpl)
# Complete non versionned cr_deploy.env
secret_dpl ?= docker-files/secrets/cr_deploy.env
include $(secret_dpl)
DOCKER_FOLDER=docker-files
export $(shell sed 's/=.*//' $(dpl))

# grep the version from the mix file
BRANCH=$(shell git rev-parse --abbrev-ref HEAD)
TAG := "$(TICKER)/$(BRANCH)"
APP_NAME := $(TICKER)_$(BRANCH)
# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build -f $(DOCKER_FOLDER)/Dockerfile -t $(TAG) .

build-nc: ## Build the container without caching
	docker build --no-cache -f $(DOCKER_FOLDER)/Dockerfile -t $(TAG) .

run: ## Run container on port configured in `config.env`
	sh $(DOCKER_FOLDER)/run.sh $(APP_NAME) $(TAG):$(VERSION)

deploy-latest: stop ## Deploy container on server
	sh $(DOCKER_FOLDER)/deploy.sh $(APP_NAME) $(DOCKER_REPO)/$(TAG):latest

test: ## Run container test command
	sh $(DOCKER_FOLDER)/test.sh $(APP_NAME)


shell: ## Access container by shell
	docker exec -ti $(APP_NAME) bash

runserver: ## Access container by shell
	sh $(DOCKER_FOLDER)/runserver.sh $(APP_NAME)

up: build stop run ## Run container on port configured in `config.env` (Alias to run)

stop: ## Stop and remove a running container
	sh $(DOCKER_FOLDER)/stop.sh $(APP_NAME)

release: build-nc publish ## Make a release by building and publishing the `{version}` ans `latest` tagged containers to ECR

# Docker publish
publish: repo-login publish-latest publish-version ## Publish the `{version}` ans `latest` tagged containers to ECR

publish-latest: repo-login tag-latest ## Publish the `latest` taged container to WCR
	@echo 'publish latest to $(DOCKER_REPO)'
	docker push $(DOCKER_REPO)/$(TAG):latest

publish-version: repo-login tag-version ## Publish the `{version}` taged container to ECR
	@echo 'publish $(VERSION) to $(DOCKER_REPO)'
	docker push $(DOCKER_REPO)/$(TAG):$(VERSION)

# Docker tagging
tag: tag-latest tag-version ## Generate container tags for the `{version}` ans `latest` tags

tag-latest: ## Generate container `{version}` tag
	@echo 'create tag latest'
	docker tag $(TAG):latest $(DOCKER_REPO)/$(TAG):latest

tag-version: ## Generate container `latest` tag
	@echo 'create tag $(VERSION)'
	docker tag $(TAG):$(VERSION) $(DOCKER_REPO)/$(TAG):$(VERSION)

# HELPERS

# generate script to login to aws docker repo
CMD_REPOLOGIN := "echo $(DOCKER_PASSWORD)|docker login -u $(DOCKER_USER) --password-stdin $(DOCKER_REPO)"

# login to DOCKER-CR
repo-login: ## Auto login to DOCKER-CR
	@eval $(CMD_REPOLOGIN)

version: ## Output the current version
	@echo $(VERSION)
