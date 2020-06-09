.SILENT:
.DEFAULT_GOAL := help

## Installs a development environment
install: deploy

## Composes project using docker-compose
deploy:
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml down -v
	docker-compose -f docker-compose.yml up -d --force-recreate

## Prints help message
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

