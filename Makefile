install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py

format:
	black *.py && black test_*.py

lint:
	ruff check test_*.py && ruff check *.py

deploy:
	# deploy goes here
		
all: install lint test format