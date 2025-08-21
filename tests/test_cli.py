from typer.testing import CliRunner
import pandas as pd

from guadalupe_weather.cli import cli
import geci_test_tools as gtt

runner = CliRunner()


def test_remove_outliers():
    input_path = "tests/data/estaciones_metereologicas_guadalupe_for_tests.csv"
    column_name = "Temp_Out"
    result = runner.invoke(
        cli, ["remove-outliers", "--input-path", input_path, "--column-name", column_name]
    )
    assert result.exit_code == 0
    expected_path = "no_outliers_estaciones_metereologicas_guadalupe_for_tests.csv"
    gtt.assert_exist(expected_path)
    obtained = pd.read_csv(expected_path)
    assert obtained.loc[9, "Temp_Out"].isna()


def test_version():
    result = runner.invoke(cli, ["version"])
    expected_version = "0.1.0"
    assert expected_version in result.stdout
