from guadalupe_weather.get_weather_data import (
    get_box_plot_data_temperature,
    get_box_plot_data,
    get_data_by_year,
    get_monthly_and_annual_average_cumulative_rain_by_zone,
    get_monthly_average_cumulative_rain_by_zone,
    get_monthly_cumulative_rain_by_year,
    get_monthly_temperature_by_year,
    get_multiannual_monthly_cumulative_rain,
)

from guadalupe_weather.plot_weather_variables import (
    get_months_labels_list,
    get_string_label_temperature,
    get_string_label,
    plot_average_rain_by_zone,
    plot_average_temperature_by_zone,
)

import calendar
import hashlib
import os
import pandas as pd
import numpy as np
import matplotlib as plt


def test_get_months_labels_list():
    obtained_list = get_months_labels_list()
    expected_list = calendar.month_name[1:]
    assert obtained_list == expected_list


def _get_hash_from_file(png_path):
    file_content = open(png_path, "rb").read()
    obtained_hash = hashlib.md5(file_content).hexdigest()
    return obtained_hash


def test_get_data_by_year():
    year = 2017
    monthly_average_rain_path = "tests/data/input_plot_average_rain_by_zone.csv"
    expected_rain_data_by_year = pd.read_csv("tests/data/rain_2017_data_by_zone.csv")
    obtained_rain_data_by_year = get_data_by_year(monthly_average_rain_path, year)
    pd.testing.assert_frame_equal(
        obtained_rain_data_by_year.reset_index(drop=True),
        expected_rain_data_by_year.reset_index(drop=True),
    )
    year = 2018
    expected_rain_data_by_year = pd.DataFrame(columns=obtained_rain_data_by_year.columns)
    obtained_rain_data_by_year = get_data_by_year(monthly_average_rain_path, year)
    pd.testing.assert_frame_equal(
        obtained_rain_data_by_year.reset_index(drop=True),
        expected_rain_data_by_year.reset_index(drop=True),
        check_dtype=False,
    )


def test_get_monthly_average_cumulative_rain_by_zone():
    output_get_data_by_year = pd.read_csv("tests/data/rain_2017_data_by_zone.csv")
    expected_january_monthly_average = 20.6
    obtained_january_monthly_average = get_monthly_average_cumulative_rain_by_zone(
        output_get_data_by_year
    )[1]
    assert expected_january_monthly_average == obtained_january_monthly_average
    expected_february_monthly_average = 5
    obtained_february_monthly_average = get_monthly_average_cumulative_rain_by_zone(
        output_get_data_by_year
    )[2]
    assert expected_february_monthly_average == obtained_february_monthly_average


def tests_get_monthly_cumulative_rain_by_year():
    year = 2017
    monthly_average_rain_path = "tests/data/input_plot_average_rain_by_zone.csv"
    obtained_data_to_plot = get_monthly_cumulative_rain_by_year(monthly_average_rain_path, year)
    expected_length_data_to_plot = 10
    obtained_length_data_to_plot = len(obtained_data_to_plot)
    assert expected_length_data_to_plot == obtained_length_data_to_plot


def test_get_monthly_and_annual_average_cumulative_rain_by_zone():
    data = pd.read_csv("tests/data/input_plot_average_rain_by_zone.csv")
    obtained_data = get_monthly_and_annual_average_cumulative_rain_by_zone(data)
    print(obtained_data)
    obtained_average_rain_jannuary_2017 = obtained_data[obtained_data["Year"] == 2017][
        "Cumulative_rain"
    ][0]
    expected_average_rain_jannuary_2017 = 20.6
    assert obtained_average_rain_jannuary_2017 == expected_average_rain_jannuary_2017


def test_get_box_plot_data():
    monthly_average_rain_path = "tests/data/input_plot_average_rain_by_zone.csv"
    monthly_average_rain_df = pd.read_csv(monthly_average_rain_path)
    obtained_box_plot_data = get_box_plot_data(monthly_average_rain_df)
    obtained_january_box_plot_data = obtained_box_plot_data[0]
    expected_january_box_plot_data = np.array([30.8, 0.0, 10.4, 0.0])
    assert (obtained_january_box_plot_data == expected_january_box_plot_data).all()
    obtained_april_box_plot_data = obtained_box_plot_data[3]
    expected_april_box_plot_data = np.array([0.2, 4.29, 5.6, 0.0])
    assert (obtained_april_box_plot_data == expected_april_box_plot_data).all()


def test_get_string_label():
    year = 2017
    obtained_string_label = get_string_label(year)
    expected_string_label = "Rain in 2017"
    assert obtained_string_label == expected_string_label, "Just an integer"
    years_list = [2017, 2018]
    obtained_string_label = get_string_label(years_list)
    expected_string_label = "Rain in (2017, 2018)"
    assert obtained_string_label == expected_string_label, "List of years"


def test_get_string_label_temperature():
    year = 2017
    obtained_string_label = get_string_label_temperature(year)
    expected_string_label = "Temperature in 2017"
    assert obtained_string_label == expected_string_label, "Just an integer"
    years_list = [2017, 2018]
    obtained_string_label = get_string_label_temperature(years_list)
    expected_string_label = "Temperature in (2017, 2018)"
    assert obtained_string_label == expected_string_label, "List of years"


def test_plot_average_temperature_hash():
    png_path = "tests/data/temperature_norte_bosque_2017.png"
    expected_hash = "6a8492c74864eb46b1cbd1cad734949b"
    if os.path.exists(png_path):
        os.remove(png_path)
    year = 2017
    monthly_average_rain_path = "tests/data/input_plot_average_rain_by_zone.csv"
    data_to_plot = get_monthly_temperature_by_year(monthly_average_rain_path, year)
    monthly_average_rain_df = pd.read_csv(monthly_average_rain_path)
    box_plot_data = get_box_plot_data_temperature(monthly_average_rain_df)
    plot_average_temperature_by_zone(data_to_plot, box_plot_data, png_path, year)
    obtained_hash = _get_hash_from_file(png_path)
    assert obtained_hash == expected_hash, f"El hash de la figura {png_path}"

    png_path = "tests/data/temperature_norte_bosque_multianual.png"
    expected_hash = "443261dffc62e08b6cc63b253431767f"
    years_list = [2017, 2021]
    if os.path.exists(png_path):
        os.remove(png_path)
    data_to_plot = pd.read_csv("tests/data/multiannual_monthly_temperature.csv", index_col=0)
    plot_average_temperature_by_zone(data_to_plot, box_plot_data, png_path, years_list)
    obtained_hash = _get_hash_from_file(png_path)
    assert obtained_hash == expected_hash, f"El hash de la figura {png_path}"


def test_plot_average_rain_hash():
    png_path = "tests/data/cumulative_rain_norte_bosque_2017.png"
    year = 2017
    monthly_average_rain_path = "tests/data/input_plot_average_rain_by_zone.csv"
    data_to_plot = get_monthly_cumulative_rain_by_year(monthly_average_rain_path, year)
    monthly_average_rain_df = pd.read_csv(monthly_average_rain_path)
    box_plot_data = get_box_plot_data(monthly_average_rain_df)
    obtained = plot_average_rain_by_zone(data_to_plot, box_plot_data, png_path, year)

    assert isinstance(obtained, plt.axes._axes.Axes)

    expected_ylabel = "Monthly rainfall (mm/month)"
    obtained_ylabel = obtained.get_ylabel()
    assert obtained_ylabel == expected_ylabel

    expected_ylim = (-0.1, 50)
    obtained_ylim = obtained.get_ylim()
    assert obtained_ylim == expected_ylim

    obtained_xticks_len = len(obtained.get_xticklabels())
    expected_xticks_len = 13
    assert obtained_xticks_len == expected_xticks_len

    obtained_last_xtick_text = obtained.get_xticklabels()[11].get_text()
    expected_last_xtick_text = "December"
    assert obtained_last_xtick_text == expected_last_xtick_text

    png_path = "tests/data/cumulative_rain_norte_bosque_multianual.png"
    expected_hash = "5a1467b7a0cfc082a3ab0d634dac0cf1"
    years_list = [2017, 2021]
    if os.path.exists(png_path):
        os.remove(png_path)
    data_to_plot = pd.read_csv("tests/data/multiannual_monthly_cumulative_rain.csv", index_col=0)
    plot_average_rain_by_zone(data_to_plot, box_plot_data, png_path, years_list)
    obtained_hash = _get_hash_from_file(png_path)
    assert obtained_hash == expected_hash, f"El hash de la figura {png_path}"


def test_get_multiannual_monthly_cumulative_rain():
    monthly_average_rain_path = "tests/data/input_plot_average_rain_by_zone.csv"
    years = [2017, 2021]
    obtained_multianual_monthly_cumulative_rain = get_multiannual_monthly_cumulative_rain(
        monthly_average_rain_path, years
    )
    obtained_january_cumulative_rain = obtained_multianual_monthly_cumulative_rain.iloc[0]
    expected_january_cumulative_rain = 10.3
    assert obtained_january_cumulative_rain == expected_january_cumulative_rain
    obtained_september_cumulative_rain = obtained_multianual_monthly_cumulative_rain.iloc[8]
    expected_september_cumulative_rain = 8.065
    assert obtained_september_cumulative_rain == expected_september_cumulative_rain
