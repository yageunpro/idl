.PHONY: dependency, genrate, run

all: dependency generate

dependency:
	@pip install fastapi uvicorn pyyaml "pydantic[email]"

generate:
	@python3 ./openapi/generate.py --app-dir ./openapi app:app --out ./openapi.yaml

run:
	uvicorn --app-dir ./openapi --reload app:app
