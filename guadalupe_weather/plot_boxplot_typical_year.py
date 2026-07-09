from guadalupe_weather.plot_weather_variables import (
    format_axis_elements,
    get_string_label_temperature,
    get_string_label_rain,
)

from geci_plots import geci_plot
import numpy as np
import matplotlib.pyplot as plt


def plot_boxplot_typical_year(boxplot_limits_df):
    config_by_variable = {
        "temperature": {
            "y_label": r"Temperature ($^{\circ}C$)",
            "box_label": "Temperature typical year",
            "y_lim_max": 30,
        },
        "rain": {
            "y_label": "Monthly rainfall (mm/month)",
            "box_label": "Rain typical year",
            "y_lim_max": 50,
        },
    }
    variable = "temperature"
    config = config_by_variable[variable]
    fontsize = 20
    fig, ax = geci_plot()
    box_plot = ax.boxplot(boxplot_limits_df, patch_artist=True, boxprops=dict(facecolor="white"))
    handles, labels = ax.get_legend_handles_labels()
    plt.legend(
        [*handles, box_plot["boxes"].pop()], [*labels, config["box_label"]], fontsize=fontsize
    )
    format_axis_elements(config, fontsize, ax)
    return ax
