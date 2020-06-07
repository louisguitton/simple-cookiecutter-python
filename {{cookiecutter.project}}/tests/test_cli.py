"""Test cases for the cli module."""
import click.testing
import pytest

from {{cookiecutter.project_slug}} import cli


@pytest.fixture
def runner():
    """CLI fixture."""
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    """It exits with status code 0."""
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
