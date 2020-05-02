# simple-cookiecutter-python

> An opinionated cookiecutter to start a python project on the right foot.

![Platform](https://img.shields.io/badge/python-3.7-blue.svg)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

For every new repo I started, I ended up re-writing the same things over and over again until I got tired
and learned how `cookiecutter` can help in this situation.

## Usage

```sh
pip install cookiecutter
cookiecutter https://github.com/louisguitton/simple-cookiecutter-python.git
```

## Features

- Python package with CLI entrypoint
- Convenient make commands for managing the python package
- pre-commit hooks with black formatting
- CI/CD boilerplate for Github and Gitlab
- Dockerfile that uses alpine
