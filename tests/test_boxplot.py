from guadalupe_weather.plot_boxplot_typical_year import plot_boxplot_typical_year
from guadalupe_weather.get_weather_data import get_box_plot_data_temperature


import pandas as pd
import matplotlib as plt


def test_plot_boxplot_typical_year():
    monthly_average_rain_path = "tests/data/input_plot_average_rain_by_zone.csv"
    monthly_average_rain_df = pd.read_csv(monthly_average_rain_path)
    boxplot_data = get_box_plot_data_temperature(monthly_average_rain_df)
    obtained = plot_boxplot_typical_year(boxplot_data)

    assert isinstance(obtained, plt.axes._axes.Axes)
