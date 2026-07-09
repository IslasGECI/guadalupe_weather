from geci_plots import geci_plot


def plot_boxplot_typical_year(boxplot_limits_df):
    fig, ax = geci_plot()
    ax.boxplot(boxplot_limits_df, patch_artist=True, boxprops=dict(facecolor="white"))
    return ax
