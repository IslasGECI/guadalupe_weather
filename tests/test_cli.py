from guadalupe_weather.cli import cli
import geci_test_tools as gtt

from typer.testing import CliRunner
import pandas as pd
import numpy as np

runner = CliRunner()


def test_render_rain_across_year():
    output_path = "tests/data/cumulative_rain_norte_bosque_2017.png"
    expected_hash = "376512ca588928fed5b10d9325b5317f"
    gtt.if_exist_remove(output_path)
    year = 2017
    input_path = "tests/data/input_plot_average_rain_by_zone.csv"
    result = runner.invoke(
        cli,
        [
            "render-rain-across-year",
            "--input-path",
            input_path,
            "--years",
            year,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    obtained_hash = gtt.calculate_hash(output_path)
    assert obtained_hash == expected_hash, f"El hash de la figura {output_path}"

    expected_hash = "5a1467b7a0cfc082a3ab0d634dac0cf1"
    output_path = "tests/multiannual_rain.png"
    gtt.if_exist_remove(output_path)
    input_path = "tests/data/input_plot_average_rain_by_zone.csv"
    result = runner.invoke(
        cli,
        [
            "render-rain-across-year",
            "--input-path",
            input_path,
            "--years",
            2017,
            "--years",
            2021,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    obtained_hash = gtt.calculate_hash(output_path)
    assert obtained_hash == expected_hash, f"El hash de la figura {output_path}"


def test_render_temperature_across_year():
    output_path = "tests/data/temperature_norte_bosque_2017.png"
    expected_hash = "6a8492c74864eb46b1cbd1cad734949b"
    gtt.if_exist_remove(output_path)
    year = 2017
    input_path = "tests/data/input_plot_average_rain_by_zone.csv"
    result = runner.invoke(
        cli,
        [
            "render-temperature-across-year",
            "--input-path",
            input_path,
            "--years",
            year,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    obtained_hash = gtt.calculate_hash(output_path)
    assert obtained_hash == expected_hash, f"El hash de la figura {output_path}"

    expected_hash = "443261dffc62e08b6cc63b253431767f"
    output_path = "tests/multiannual_temperature.png"
    gtt.if_exist_remove(output_path)
    result = runner.invoke(
        cli,
        [
            "render-temperature-across-year",
            "--input-path",
            input_path,
            "--years",
            2017,
            "--years",
            2021,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    obtained_hash = gtt.calculate_hash(output_path)
    assert obtained_hash == expected_hash, f"El hash de la figura {output_path}"


def test_remove_outliers():
    input_path = "tests/data/estaciones_meteorologicas_guadalupe_for_tests.csv"
    output_path = "tests/no_outliers_estaciones_meteorologicas_guadalupe_for_tests.csv"
    result = runner.invoke(
        cli,
        [
            "remove-outliers",
            "--input-path",
            input_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    obtained = pd.read_csv(output_path)
    assert obtained.shape == (10, 39)
    assert np.isnan(obtained.loc[9, "Temp_Out"])
    assert "Temp_Out limits" in result.stdout


def test_remove_outliers_for_column():
    input_path = "tests/data/estaciones_meteorologicas_guadalupe_for_tests.csv"
    column_name = "Temp_Out"
    output_path = "tests/no_outliers_estaciones_meteorologicas_guadalupe_for_tests.csv"
    result = runner.invoke(
        cli,
        [
            "remove-outliers-for-column",
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
    assert "Temp_Out limits" in result.stdout


def test_version():
    result = runner.invoke(cli, ["version"])
    expected_version = "0.3.1"
    assert expected_version in result.stdout
