"""{{cookiecutter.project_slug}} module."""
import logging

from rich.logging import RichHandler


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(RichHandler())