import pathlib
from setuptools import setup, find_packages


def read(fname):
    with open(pathlib.Path(fname)) as fh:
        data = fh.read()
    return data


base_packages = ["Click>=7.0"]

dev_packages = [
    "jupyterlab>=0.35.4",
    "pytest>=4.0.2",
    "black>=19.3b0",
    "flake8>=3.6.0",
    "pre-commit>=2.2.0",
    "mkdocs>=1.1",
    "mkdocs-material==4.6.3",
    "mkdocstrings>=0.11.0",
]

setup(
    name="{{ cookiecutter.project_slug }}",
    version="0.0.1",
    packages=find_packages(exclude=["data", "docs", "notebooks"]),
    long_description=read("readme.md"),
    install_requires=base_packages,
    entry_points={"console_scripts": ["app_review_topics = app_review_topics.cli:cli"]},
    extras_require={"dev": dev_packages},
)
