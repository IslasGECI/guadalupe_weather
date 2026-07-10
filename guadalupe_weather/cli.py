from guadalupe_weather.get_outliers import (
    _remove_outliers,
    _remove_outliers_for_column,
)
from guadalupe_weather.get_weather_data import (
    get_boxplot_data,
    get_multiannual_monthly_cumulative_rain,
    get_multiannual_monthly_temperature,
    get_boxplot_data_without_nan,
)
from guadalupe_weather.plot_weather_variables import (
    plot_average_rain_by_zone,
    plot_average_temperature_by_zone,
)
from guadalupe_weather.plot_boxplot_typical_year import plot_boxplot_typical_year
from guadalupe_weather import __version__

import typer
from typing_extensions import Annotated
import pandas as pd
from typing import List
import matplotlib.pyplot as plt

cli = typer.Typer()


@cli.command()
def render_typical_year_boxplot(
    input_path: Annotated[str, typer.Option()],
    variable_of_interest: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    config_by_variable = {
        "Avg_Temp_Out": {
            "y_label": r"Temperature ($^{\circ}C$)",
            "box_label": "Temperature typical year",
            "y_lim_max": 30,
            "boxplot_method": get_boxplot_data_without_nan,
        },
        "Cumulative_rain": {
            "y_label": "Monthly rainfall (mm/month)",
            "box_label": "Rain typical year",
            "y_lim_max": 50,
            "boxplot_method": get_boxplot_data,
        },
    }
    monthly_average_df = pd.read_csv(input_path)
    config = config_by_variable.get(variable_of_interest)
    box_plot_data = config["boxplot_method"](monthly_average_df, variable_of_interest)
    plot_boxplot_typical_year(box_plot_data, config)
    plt.savefig(output_path, dpi=300)


@cli.command()
def render_temperature_across_year(
    input_path: Annotated[str, typer.Option()],
    years: Annotated[List[int], typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    monthly_average_df = pd.read_csv(input_path)
    variable = "Avg_Temp_Out"
    data_to_plot = get_multiannual_monthly_temperature(monthly_average_df, years)
    box_plot_data = get_boxplot_data_without_nan(monthly_average_df, variable)
    plot_average_temperature_by_zone(data_to_plot, box_plot_data, years)
    plt.savefig(output_path, dpi=300)


@cli.command()
def render_rain_across_year(
    input_path: Annotated[str, typer.Option()],
    years: Annotated[List[int], typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    monthly_average_rain_df = pd.read_csv(input_path)
    data_to_plot = get_multiannual_monthly_cumulative_rain(monthly_average_rain_df, years)
    variable = "Cumulative_rain"
    box_plot_data = get_boxplot_data(monthly_average_rain_df, variable)
    plot_average_rain_by_zone(data_to_plot, box_plot_data, years)
    plt.savefig(output_path, dpi=300)


@cli.command()
def remove_outliers(
    input_path: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    data = pd.read_csv(input_path)
    no_outliers_df = _remove_outliers(data)
    no_outliers_df.to_csv(output_path, index=False)


@cli.command()
def remove_outliers_for_column(
    input_path: Annotated[str, typer.Option()],
    column_name: Annotated[str, typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    data = pd.read_csv(input_path)
    no_outliers_df = _remove_outliers_for_column(data, column_name)
    no_outliers_df.to_csv(output_path, index=False)


@cli.command()
def version():
    print(__version__)
