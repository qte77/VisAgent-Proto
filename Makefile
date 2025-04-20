.PHONY: all

all: setup_dev

setup_prod: ## Install uv and deps
	@echo "Setting up prod tools..."
	@pip install uv
	@uv sync --frozen

setup_dev: ## Install uv and developer dependencies
	@echo "Setting up dev tools..."
	@pip install uv
	@uv sync --all-groups --frozen

ruff: ## Lint: Format and check with ruff
	@uv run ruff format
	@uv run ruff check --fix

type_check: ## Check for static typing errors
	@uv run mypy src

help:
	@echo "Usage: make [recipe]"
	@echo "Recipes:"
	@awk '/^[a-zA-Z0-9_-]+:.*?##/ { \
		helpMessage = match($$0, /## (.*)/); \
		if (helpMessage) { \
			recipe = $$1; \
			sub(/:/, "", recipe); \
			printf "  \033[36m%-20s\033[0m %s\n", recipe, substr($$0, RSTART + 3, RLENGTH); \
		} \
	}' $(MAKEFILE_LIST)