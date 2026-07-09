from guadalupe_weather.get_outliers import (
    _remove_outliers,
    _remove_outliers_for_column,
)
from guadalupe_weather.get_weather_data import (
    get_multiannual_monthly_cumulative_rain,
    get_box_plot_data,
)
from guadalupe_weather.plot_weather_variables import plot_average_rain_by_zone
import guadalupe_weather as gw

import typer
from typing_extensions import Annotated
import pandas as pd
from typing import List
import matplotlib.pyplot as plt

cli = typer.Typer()


@cli.command()
def render_rain_across_year(
    input_path: Annotated[str, typer.Option()],
    years: Annotated[List[int], typer.Option()],
    output_path: Annotated[str, typer.Option()],
):
    monthly_average_rain_df = pd.read_csv(input_path)
    data_to_plot = get_multiannual_monthly_cumulative_rain(input_path, years)
    box_plot_data = get_box_plot_data(monthly_average_rain_df)
    plot_average_rain_by_zone(data_to_plot, box_plot_data, output_path, years)
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
    print(gw.__version__)
