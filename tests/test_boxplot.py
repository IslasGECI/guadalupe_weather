from guadalupe_weather.plot_boxplot_typical_year import plot_boxplot_typical_year
from guadalupe_weather.get_weather_data import get_box_plot_data_temperature


import matplotlib as plt
import numpy as np


def test_plot_boxplot_typical_year():
    boxplot_data = [np.random.rand(np.random.randint(1, 10)) for _ in range(12)]
    obtained = plot_boxplot_typical_year(boxplot_data)
    plt.pyplot.savefig("tests/data/boxplot_typical_year.png", dpi=300)

    assert isinstance(obtained, plt.axes._axes.Axes)
