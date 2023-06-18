.PHONY: run

run:
	@echo "Running the app..."
	uvicorn app.main:app --reload --port 8000