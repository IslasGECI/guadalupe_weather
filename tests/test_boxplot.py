from guadalupe_weather.plot_boxplot_typical_year import plot_boxplot_typical_year


import matplotlib as plt
import numpy as np


def test_plot_boxplot_typical_year():
    boxplot_data = [np.random.rand(np.random.randint(1, 10)) for _ in range(12)]
    expected_ylabel = "Y label (units)"
    expected_box_label = "Box label"
    expected_ylim = 1
    config = {
        "y_label": expected_ylabel,
        "box_label": expected_box_label,
        "y_lim_max": expected_ylim,
    }
    obtained = plot_boxplot_typical_year(boxplot_data, config)
    plt.pyplot.savefig("tests/data/boxplot_typical_year.png", dpi=300)
    assert isinstance(obtained, plt.axes._axes.Axes)

    obtained_last_xtick_text = obtained.get_xticklabels()[0].get_text()
    expected_last_xtick_text = "January"
    assert obtained_last_xtick_text == expected_last_xtick_text

    obtained_ylabel = obtained.get_ylabel()
    assert obtained_ylabel == expected_ylabel

    obtained_ylim = obtained.get_ylim()
    assert obtained_ylim[1] == expected_ylim

    obtained_legend_texts = [text.get_text() for text in obtained.get_legend().get_texts()]
    expected_legend_texts = [expected_box_label]
    assert obtained_legend_texts == expected_legend_texts
