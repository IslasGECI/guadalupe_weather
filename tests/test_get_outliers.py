from guadalupe_weather.get_outliers import (
    get_outliers,
    remove_outliers_for_column,
    get_tukey_fences_by_daily_means_for_variables_of_interest,
    get_tukey_fences_by_daily_max_and_min,
    get_tukey_fences_by_variable,
)
import pandas as pd
import numpy as np

outlier = 50
data = pd.DataFrame(
    {
        "Date": [
            "30/Sep/2008",
            "30/Sep/2008",
            "30/Sep/2008",
            "30/Sep/2008",
            "30/Sep/2008",
            "30/Sep/2008",
            "30/Sep/2008",
            "30/Sep/2008",
            "30/Sep/2008",
            "30/Sep/2008",
            "30/Sep/2008",
            "01/Oct/2008",
            "01/Oct/2008",
            "01/Oct/2008",
        ],
        "Variable": [2, 3, 5, 7, 9, 11, 14, 18, 22, outlier, np.nan, 1, 2, 3],
        "Variable2": [np.nan, 2, 3, 5, 7, 9, 11, 14, 18, outlier, 22, 1, 2, 3],
    }
)


def test_get_outliers():
    superior_limit = 25
    inferior_limit = 0
    obtained = get_outliers(data.Variable, inferior_limit, superior_limit)
    assert obtained == [outlier]


def tests_remove_outliers():
    column_name = "Variable"
    obtained = remove_outliers_for_column(data, column_name)

    assert obtained.shape == data.shape
    assert np.isnan(obtained[column_name].iloc[-5])
    assert np.isnan(obtained[column_name].iloc[-6])


def test_get_tukey_fences_by_daily_means_for_variables_of_interest():
    variables_of_interest = ["Variable", "Variable2"]
    obtained = get_tukey_fences_by_daily_means_for_variables_of_interest(
        data, variables_of_interest
    )
    assert np.shape(obtained) == (2, 2)


def test_get_tukey_fences_by_daily_max_and_min():
    column_name = "Variable"
    obtained_max_inferior, obtained_max_superior, obtained_min_inferior, obtained_min_superior = (
        get_tukey_fences_by_daily_max_and_min(data, column_name)
    )
    assert obtained_max_inferior == -20.5
    assert obtained_max_superior == 73.5
    assert obtained_min_inferior == 0.5
    assert obtained_min_superior == 2.5


def test_get_tukey_fences_by_variable():
    variable = "Rain"
    data = pd.read_csv("tests/data/estaciones_meteorologicas_guadalupe_for_tests.csv")
    obtained_inferior, obtained_superior = get_tukey_fences_by_variable(data, variable)
    assert obtained_inferior == 0
    assert obtained_superior == 449.25
    variable = "Dew_Pt"
    obtained_inferior, obtained_superior = get_tukey_fences_by_variable(data, variable)
    assert obtained_inferior == -4
    assert obtained_superior == 17.1
