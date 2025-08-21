from typer.testing import CliRunner
import pandas as pd
import numpy as np

from guadalupe_weather.cli import cli
import geci_test_tools as gtt

runner = CliRunner()


def test_remove_outliers():
    input_path = "tests/data/estaciones_meteorologicas_guadalupe_for_tests.csv"
    column_name = "Temp_Out"
    output_path = "tests/no_outliers_estaciones_meteorologicas_guadalupe_for_tests.csv"
    result = runner.invoke(
        cli,
        [
            "remove-outliers",
            "--input-path",
            input_path,
            "--column-name",
            column_name,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    obtained = pd.read_csv(output_path)
    assert obtained.shape == (10, 39)
    assert np.isnan(obtained.loc[9, "Temp_Out"])
    assert "(Inferior: 10.99, Superior: 43.67)" in result.stdout


def test_version():
    result = runner.invoke(cli, ["version"])
    expected_version = "0.2.2"
    assert expected_version in result.stdout
