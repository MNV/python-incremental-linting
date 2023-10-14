.DEFAULT_GOAL := help
TARGET = origin/main

.PHONY: help
help: ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint: ## Static analysis for modified files
	# code quality check
	./git-diff-lint -x "ruff check --exit-zero" -b $(TARGET)
	# code style check
	darker --revision $(TARGET) --diff --check

.PHONY:	fix
fix: ## Fixing modified files
	# code formatting
	darker --revision $(TARGET)
	# try to fix detected code flaws
	./git-diff-lint -x "ruff --fix --silent --exit-zero" -b $(TARGET)
