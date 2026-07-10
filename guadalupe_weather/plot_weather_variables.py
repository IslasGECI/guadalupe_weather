import calendar
import numpy as np
import matplotlib.pyplot as plt

from geci_plots import geci_plot
from guadalupe_weather.plot_boxplot_typical_year import add_boxplot
from guadalupe_weather.fortmat_axis_elements import format_axis_elements


def plot_average_rain_by_zone(data_to_plot, box_plot_data, year_list):
    variable = "Rain"
    ax = plot_average_and_boxplot_by_variable(data_to_plot, box_plot_data, variable, year_list)
    return ax


def plot_average_temperature_by_zone(data_to_plot, box_plot_data, year_list):
    variable = "Temperature"
    ax = plot_average_and_boxplot_by_variable(data_to_plot, box_plot_data, variable, year_list)
    return ax


def plot_average_and_boxplot_by_variable(data_to_plot, box_plot_data, variable, year_list):
    config_by_variable = {
        "Temperature": {
            "y_label": r"Temperature ($^{\circ}C$)",
            "box_label": "Temperature typical year",
            "y_lim_max": 30,
        },
        "Rain": {
            "y_label": "Monthly rainfall (mm/month)",
            "box_label": "Rain typical year",
            "y_lim_max": 50,
        },
    }
    config = config_by_variable[variable]
    fontsize = 20
    fig, ax = geci_plot()
    box_plot = add_boxplot(box_plot_data, config, fontsize, ax)
    string_label = get_string_label_for_variable(variable, year_list)
    ax.plot(
        data_to_plot.index,
        data_to_plot.values,
        "-o",
        linewidth=2,
        markeredgecolor="k",
        markersize=5,
        label=string_label,
    )
    handles, labels = ax.get_legend_handles_labels()
    plt.legend(
        [*handles, box_plot["boxes"].pop()], [*labels, config["box_label"]], fontsize=fontsize
    )
    format_axis_elements(config, fontsize, ax)
    return ax


def get_string_label_temperature(years):
    variable = "Temperature"
    return get_string_label_for_variable(variable, years)


def get_string_label_rain(years):
    variable = "Rain"
    return get_string_label_for_variable(variable, years)


def get_string_label_for_variable(variable, years):
    if len(years) > 1:
        return f"{variable} in {*years, }"
    return f"{variable} in {years[0]}"
