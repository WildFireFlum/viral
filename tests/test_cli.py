import pytest
from typer.testing import CliRunner

from viral import (
    SUCCESS,
    __app_name__,
    __version__,
    cli,
)


@pytest.fixture()
def cli_runner(request) -> CliRunner:
    """
    Return a new instanse of CliRunner.
    """
    return CliRunner()


def test_version(cli_runner):
    result = cli_runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}" in result.stdout

