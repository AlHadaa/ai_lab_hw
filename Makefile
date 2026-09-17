# ==============================================================================
# Makefile: Project Automation & Linux Workflow Helper
# Course: AI Lab - Dr. Mohammed Al-Dhobaie
# ==============================================================================

.PHONY: help setup run test clean health

help:
	@echo "Available commands:"
	@echo "  make setup   - Set up virtual environment and install requirements"
	@echo "  make run     - Run the web application server"
	@echo "  make test    - Run automated unit tests with pytest"
	@echo "  make health  - Perform Linux curl health checks against running server"
	@echo "  make clean   - Remove cache files and build artifacts"

setup:
	bash scripts/setup.sh

run:
	python run.py

test:
	pytest -v tests/

health:
	bash scripts/health_check.sh

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
