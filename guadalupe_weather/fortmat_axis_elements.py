import calendar
import numpy as np
import matplotlib.pyplot as plt


def format_axis_elements(config, fontsize, ax):
    ticks_positions = np.linspace(1, 12, 12)
    months_labels = get_months_labels_list()
    plt.xticks([*ticks_positions, 13], [*months_labels, ""], size=fontsize, rotation=90)
    plt.yticks(size=fontsize)
    plt.ylabel(config["y_label"], size=fontsize)
    y_lim_min = -0.1
    ax.set_ylim(
        y_lim_min,
        config["y_lim_max"],
    )
    plt.tight_layout()


def get_months_labels_list() -> list:
    return list(calendar.month_name[1:])
