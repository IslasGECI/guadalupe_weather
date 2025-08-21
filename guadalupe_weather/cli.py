import typer
from typing_extensions import Annotated
import pandas as pd
import guadalupe_weather as gw

cli = typer.Typer()


@cli.command()
def remove_outliers(
    input_path: Annotated[str, typer.Option()], column_name: Annotated[str, typer.Option()]
):
    pd.DataFrame({"empty": [0, 1]}).to_csv(
        "no_outliers_estaciones_metereologicas_guadalupe_for_tests.csv"
    )


@cli.command()
def version():
    print(gw.__version__)
