.PHONY: run

run:
	@echo "Running the app..."
	uvicorn main:app --reload --port 8000