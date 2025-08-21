from guadalupe_weather.cli import cli
from typer.testing import CliRunner

runner = CliRunner()


def test_remove_outliers():
    result = runner.invoke(cli, ["remove-outliers"])
    assert result.exit_code == 0


def test_version():
    result = runner.invoke(cli, ["version"])
    expected_version = "0.1.0"
    assert expected_version in result.stdout
