from guadalupe_weather.fortmat_axis_elements import (
    format_axis_elements,
)

from geci_plots import geci_plot
import matplotlib.pyplot as plt


def plot_boxplot_typical_year(boxplot_limits_df, config):
    fontsize = 20
    fig, ax = geci_plot()
    add_boxplot(boxplot_limits_df, config, fontsize, ax)
    format_axis_elements(config, fontsize, ax)
    return ax


def add_boxplot(boxplot_limits_df, config, fontsize, ax):
    box_plot = ax.boxplot(boxplot_limits_df, patch_artist=True, boxprops=dict(facecolor="white"))
    plt.legend([box_plot["boxes"].pop()], [config["box_label"]], fontsize=fontsize)
    return box_plot
