import pandas as pd
import numpy as np


from guadalupe_weather.get_weather_data import (
    get_monthly_average_temperature_by_zone,
    get_box_plot_data_temperature,
    xxget_multiannual_monthly_temperature,
)


def test_get_monthly_average_temperature_by_zone():
    output_get_data_by_year = pd.read_csv("tests/data/rain_2017_data_by_zone.csv")
    expected_january_monthly_average = 9.25
    obtained_january_monthly_average = get_monthly_average_temperature_by_zone(
        output_get_data_by_year
    )[1]
    assert expected_january_monthly_average == obtained_january_monthly_average
    expected_february_monthly_average = 12.2
    obtained_february_monthly_average = get_monthly_average_temperature_by_zone(
        output_get_data_by_year
    )[2]
    assert expected_february_monthly_average == obtained_february_monthly_average


def test_get_box_plot_data_temperature():
    monthly_average_rain_path = "tests/data/input_plot_average_rain_by_zone.csv"
    monthly_average_rain_df = pd.read_csv(monthly_average_rain_path)
    obtained_box_plot_data = get_box_plot_data_temperature(monthly_average_rain_df)
    obtained_january_box_plot_data = obtained_box_plot_data[0]
    expected_january_box_plot_data = np.array([8.5, 14.5, 10.0])
    np.testing.assert_equal(obtained_january_box_plot_data, expected_january_box_plot_data)
    obtained_april_box_plot_data = obtained_box_plot_data[3]
    expected_april_box_plot_data = np.array([14.0, 14.6, 13.7, 17.2])
    assert (obtained_april_box_plot_data == expected_april_box_plot_data).all()


def test_get_multiannual_monthly_temperature():
    monthly_average_rain_path = "tests/data/input_plot_average_rain_by_zone.csv"
    years = [2017, 2021]
    monthly_average_rain_df = pd.read_csv(monthly_average_rain_path)
    obtained_multianual_monthly_temperature = xxget_multiannual_monthly_temperature(
        monthly_average_rain_df, years
    )
    obtained_october_temperature = obtained_multianual_monthly_temperature.iloc[9]
    expected_october_temperature = 14.4
    assert obtained_october_temperature == expected_october_temperature
    obtained_december_temperature = obtained_multianual_monthly_temperature.iloc[11]
    expected_december_temperature = 12.025
    assert obtained_december_temperature == expected_december_temperature

    years = [2017]
    obtained_data_to_plot = xxget_multiannual_monthly_temperature(monthly_average_rain_df, years)
    expected_length_data_to_plot = 10
    obtained_length_data_to_plot = len(obtained_data_to_plot)
    assert expected_length_data_to_plot == obtained_length_data_to_plot
