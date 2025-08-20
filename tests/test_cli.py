from guadalupe_weather.cli import cli
from typer.testing import CliRunner

runner = CliRunner()


def test_version():
    result = runner.invoke(
        cli,
    )
    expected_version = "0.1.0"
    assert expected_version in result.stdout
