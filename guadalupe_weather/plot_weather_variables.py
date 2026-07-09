import calendar
import numpy as np
import matplotlib.pyplot as plt

from geci_plots import geci_plot


def plot_average_rain_by_zone(data_to_plot, box_plot_data, png_path, year_list):
    variable = "rain"
    xxplot_average_and_boxplot_by_variable(data_to_plot, box_plot_data, variable, year_list)
    plt.savefig(png_path, dpi=300)


def xxplot_average_and_boxplot_by_variable(data_to_plot, box_plot_data, variable, year_list):
    config_by_variable = {
        "temperature": {
            "y_label": r"Temperature ($^{\circ}C$)",
            "string_label": get_string_label_temperature,
            "box_label": "Temperature typical year",
            "y_lim_max": 30,
        },
        "rain": {
            "y_label": "Monthly rainfall (mm/month)",
            "string_label": get_string_label,
            "box_label": "Rain typical year",
            "y_lim_max": 50,
        },
    }
    config = config_by_variable[variable]
    fontsize = 20
    ticks_positions = np.linspace(1, 12, 12)
    months_labels = get_months_labels_list()
    fig, ax = geci_plot()
    box_plot = ax.boxplot(box_plot_data, patch_artist=True, boxprops=dict(facecolor="white"))
    ax.plot(
        data_to_plot.index,
        data_to_plot.values,
        "-o",
        linewidth=2,
        markeredgecolor="k",
        markersize=5,
        label=config["string_label"](year_list),
    )
    plt.xticks([*ticks_positions, 13], [*months_labels, ""], size=fontsize, rotation=90)
    plt.yticks(size=fontsize)
    plt.ylabel(config["y_label"], size=fontsize)
    y_lim_min = -0.1
    ax.set_ylim(
        y_lim_min,
        config["y_lim_max"],
    )
    handles, labels = ax.get_legend_handles_labels()
    plt.legend(
        [*handles, box_plot["boxes"].pop()], [*labels, config["box_label"]], fontsize=fontsize
    )
    plt.tight_layout()


def plot_average_and_boxplot_by_variable(
    data_to_plot, box_plot_data, string_label, y_label, y_lim_max, box_label
):
    fontsize = 20
    ticks_positions = np.linspace(1, 12, 12)
    months_labels = get_months_labels_list()
    fig, ax = geci_plot()
    box_plot = ax.boxplot(box_plot_data, patch_artist=True, boxprops=dict(facecolor="white"))
    ax.plot(
        data_to_plot.index,
        data_to_plot.values,
        "-o",
        linewidth=2,
        markeredgecolor="k",
        markersize=5,
        label=string_label,
    )
    plt.xticks([*ticks_positions, 13], [*months_labels, ""], size=fontsize, rotation=90)
    plt.yticks(size=fontsize)
    plt.ylabel(y_label, size=fontsize)
    y_lim_min = -0.1
    ax.set_ylim(
        y_lim_min,
        y_lim_max,
    )
    handles, labels = ax.get_legend_handles_labels()
    plt.legend([*handles, box_plot["boxes"].pop()], [*labels, box_label], fontsize=fontsize)
    plt.tight_layout()


def plot_average_temperature_by_zone(data_to_plot, box_plot_data, png_path, year_list):
    variable = "temperature"
    xxplot_average_and_boxplot_by_variable(data_to_plot, box_plot_data, variable, year_list)
    plt.savefig(png_path, dpi=300)


def get_y_max_limit(all_years_data):
    return 50


def get_string_label_temperature(years):
    if isinstance(years, list):
        return f"Temperature in {*years, }"
    return f"Temperature in {years}"


def get_string_label(years):
    if isinstance(years, list):
        return f"Rain in {*years, }"
    return f"Rain in {years}"


def get_months_labels_list() -> list:
    return list(calendar.month_name[1:])
