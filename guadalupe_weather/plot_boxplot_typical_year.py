from guadalupe_weather.plot_weather_variables import get_months_labels_list

from geci_plots import geci_plot
import numpy as np
import matplotlib.pyplot as plt


def plot_boxplot_typical_year(boxplot_limits_df):
    fontsize = 20
    fig, ax = geci_plot()
    ax.boxplot(boxplot_limits_df, patch_artist=True, boxprops=dict(facecolor="white"))
    ticks_positions = np.linspace(1, 12, 12)
    months_labels = get_months_labels_list()
    plt.xticks([*ticks_positions, 13], [*months_labels, ""], size=fontsize, rotation=90)
    return ax
