
install:
	pip install -r requirements.txt
	pip install -e .

run-api:
	uvicorn central_bank_ai.main:app --reload

run-dashboard:
	streamlit run dashboard/app.py

test:
	pytest -v

lint:
	ruff check .

format:
	ruff format .

docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down
