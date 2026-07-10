from guadalupe_weather.plot_boxplot_typical_year import plot_boxplot_typical_year


import matplotlib as plt
import numpy as np


def test_plot_boxplot_typical_year():
    boxplot_data = [np.random.rand(np.random.randint(1, 10)) for _ in range(12)]
    config = {
        "y_label": r"Temperature ($^{\circ}C$)",
        "box_label": "Temperature typical year",
        "y_lim_max": 30,
    }
    obtained = plot_boxplot_typical_year(boxplot_data, config)
    plt.pyplot.savefig("tests/data/boxplot_typical_year.png", dpi=300)
    assert isinstance(obtained, plt.axes._axes.Axes)

    obtained_last_xtick_text = obtained.get_xticklabels()[0].get_text()
    expected_last_xtick_text = "January"
    assert obtained_last_xtick_text == expected_last_xtick_text
