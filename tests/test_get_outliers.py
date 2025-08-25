from guadalupe_weather.get_outliers import (
    get_outliers,
    get_tukey_fences_by_daily_max_and_min,
    get_tukey_fences_for_max_and_min_variables,
    get_tukey_fences_for_max_variables,
    get_tukey_fences_for_min_variables,
    get_tukey_fences_for_rain,
    remove_outliers_for_column,
    remove_outliers,
    TukeyMethodSelector,
)
import pandas as pd
import numpy as np
import pytest

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
        "Rain": [2, 3, 5, 7, 9, 11, 14, 18, 22, outlier, np.nan, 1, 2, 3],
        "Variable2": [np.nan, 2, 3, 5, 7, 9, 11, 14, 18, outlier, 22, 1, 2, 3],
    }
)


def test_get_outliers():
    superior_limit = 25
    inferior_limit = 0
    obtained = get_outliers(data.Rain, inferior_limit, superior_limit)
    assert obtained == [outlier]


def tests_remove_outliers_for_column():
    column_name = "Rain"
    obtained = remove_outliers_for_column(data, column_name)

    assert obtained.shape == data.shape
    assert np.isnan(obtained[column_name].iloc[-5])
    assert np.isnan(obtained[column_name].iloc[-6])

    column_name = "Variable2"
    with pytest.raises(KeyError):
        remove_outliers_for_column(data, column_name)


def tests_remove_outliers():
    data = pd.read_csv("tests/data/estaciones_meteorologicas_guadalupe_for_tests.csv")
    obtained = remove_outliers(data)
    assert obtained.Rain.isna().sum() == 1


def test_get_tukey_fences_by_daily_max_and_min():
    column_name = "Rain"
    obtained_max_inferior, obtained_max_superior, obtained_min_inferior, obtained_min_superior = (
        get_tukey_fences_by_daily_max_and_min(data, column_name)
    )
    assert obtained_max_inferior == -20.5
    assert obtained_max_superior == 73.5
    assert obtained_min_inferior == 0.5
    assert obtained_min_superior == 2.5


def test_get_tukey_fences_by_variable():
    data = pd.DataFrame(
        {
            "Date": [
                "30/Sep/2008",
                "01/Oct/2008",
                "30/Sep/2008",
                "01/Oct/2008",
                "30/Sep/2008",
                "01/Oct/2008",
                "30/Sep/2008",
                "01/Oct/2008",
                "30/Sep/2008",
                "01/Oct/2008",
            ],
            "Rain": [0, 0, 0, 2, 0, 0, 0, 0, 3, 599],
            "Dew_Pt": [17.1, 17.1, 17.1, 17.1, 17.1, 17.1, 17, 17, 17.1, 3.7],
            "Hi_Speed": [27.4, 27.4, 20.9, 20.9, 22.5, 22.5, 22.5, 22.5, 22.5, 40.8],
            "Heat_D_D": [0, 0, 0, 0, 0, 0, 0, 0, 5, 60],
        }
    )

    variable = "Rain"
    obtained_inferior, obtained_superior = get_tukey_fences_for_rain(data, variable)
    assert obtained_inferior == 0
    assert obtained_superior == 449.25

    variable = "Dew_Pt"
    obtained_inferior, obtained_superior = get_tukey_fences_for_min_variables(data, variable)
    assert pytest.approx(obtained_inferior) == -2.95
    assert pytest.approx(obtained_superior, rel=1e-3) == 23.65

    variable = "Hi_Speed"
    obtained_inferior, obtained_superior = get_tukey_fences_for_max_and_min_variables(
        data, variable
    )
    assert obtained_inferior == 20.9
    assert pytest.approx(obtained_superior, rel=1e-3) == 47.49

    variable = "Heat_D_D"
    obtained_inferior, obtained_superior = get_tukey_fences_for_max_variables(data, variable)
    assert obtained_inferior == -22.5
    assert obtained_superior == 87.5


def test_TukeyMethodSelector():
    tukey_selector = TukeyMethodSelector()

    obtained_variables = list(tukey_selector.variables.keys())
    expected_variables = [
        "Rain",
        "Rain_Rate",
        "Dew_Pt",
        "Heat_D_D",
        "Hi_Speed",
        "Wind_Chill",
        "Heat_Index",
        "Temp_Out",
        "Hi_Temp",
        "Low_Temp",
    ]
    assert obtained_variables == expected_variables

    variable = "Rain_Rate"
    obtained_method = tukey_selector.select_method(variable)
    assert obtained_method == get_tukey_fences_for_rain
    variable = "Wind_Chill"
    obtained_method = tukey_selector.select_method(variable)
    assert obtained_method == get_tukey_fences_for_max_and_min_variables
    variable = "Heat_Index"
    obtained_method = tukey_selector.select_method(variable)
    assert obtained_method == get_tukey_fences_for_max_and_min_variables
    variable = "Temp_Out"
    obtained_method = tukey_selector.select_method(variable)
    assert obtained_method == get_tukey_fences_for_max_and_min_variables
    variable = "Low_Temp"
    obtained_method = tukey_selector.select_method(variable)
    assert obtained_method == get_tukey_fences_for_max_and_min_variables
    variable = "Hi_Temp"
    obtained_method = tukey_selector.select_method(variable)
    assert obtained_method == get_tukey_fences_for_max_and_min_variables
