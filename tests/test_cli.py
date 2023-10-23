from pytest import fixture
from typer.testing import CliRunner

from viral import (
    __app_name__,
    __version__,
    cli,
)


@fixture()
def cli_runner() -> CliRunner:
    """
    Return a new instanse of CliRunner.
    """
    return CliRunner()


def test_version(cli_runner: CliRunner):
    result = cli_runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}" in result.stdout
