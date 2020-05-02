.PHONY: docs

install:
	pip install --upgrade pip
	pip install -e .

develop: install
	pip install -e ".[dev]"
	python setup.py develop
	pre-commit install

lint:
	flake8 setup.py {{ cookiecutter.project_slug }} tests --count --statistics

test:
	pytest tests

docs:
	mkdocs build --clean --site-dir public

serve-docs:
	mkdocs serve

clean:
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf scikit_lego.egg-info
	rm -rf .ipynb_checkpoints
	rm -rf notebooks/.ipynb_checkpoints

build:
	docker build -t {{ cookiecutter.project_slug }} .
