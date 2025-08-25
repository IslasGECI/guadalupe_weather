from guadalupe_weather.get_daily_mean import get_daily_mean, get_daily_max_and_min

import numpy as np
from typing import Any


def remove_outliers(data):
    data_copy = data.copy()
    tukey_selector = TukeyMethodSelector()

    for column in tukey_selector.variables.keys():
        method = tukey_selector.select_method(column)
        linf, lsup = method(data, column)
        outliers = get_outliers(data_copy[column], linf, lsup)
        data_copy[column] = data_copy[column].replace(outliers, np.nan)
    return data_copy


class TukeyMethodSelector:
    def __init__(self):
        self.variables = method_by_variable = {
            "Rain": get_tukey_fences_for_rain,
            "Rain_Rate": get_tukey_fences_for_rain,
            "Dew_Pt": get_tukey_fences_for_min_variables,
            "Heat_D_D": get_tukey_fences_for_max_variables,
            "Hi_Speed": get_tukey_fences_for_max_and_min_variables,
            "Wind_Chill": get_tukey_fences_for_max_and_min_variables,
            "Heat_Index": get_tukey_fences_for_max_and_min_variables,
            "Temp_Out": get_tukey_fences_for_max_and_min_variables,
            "Hi_Temp": get_tukey_fences_for_max_and_min_variables,
            "Low_Temp": get_tukey_fences_for_max_and_min_variables,
        }

    def select_method(self, variable):
        return self.variables[variable]


def remove_outliers_for_column(data, column_name):
    data_copy = data.copy()
    column_data = data[column_name]
    tukey_selector = TukeyMethodSelector()
    method = tukey_selector.select_method(column_name)
    linf, lsup = method(data_copy, column_name)
    outliers = get_outliers(column_data, linf, lsup)
    data_copy[column_name] = column_data.replace(outliers, np.nan)
    return data_copy


def get_tukey_fences_for_rain(data, variable):
    remove_zeros = data[data[variable] != 0]
    _, superior = get_tukey_fences_by_daily_means(remove_zeros, variable)
    return 0, superior


def get_tukey_fences_for_max_variables(data, variable):
    max_inferior, max_superior, _, _ = get_tukey_fences_by_daily_max_and_min(data, variable)
    return max_inferior, max_superior


def get_tukey_fences_for_min_variables(data, variable):
    _, _, min_inferior, min_superior = get_tukey_fences_by_daily_max_and_min(data, variable)
    return min_inferior, min_superior


def get_tukey_fences_for_max_and_min_variables(data, variable):
    _, max_superior, min_inferior, _ = get_tukey_fences_by_daily_max_and_min(data, variable)
    return min_inferior, max_superior


def get_tukey_fences_by_daily_max_and_min(data, column_name):
    daily_max_min = get_daily_max_and_min(data, column_name)
    max_inferior, max_superior = get_tukey_limits(daily_max_min["max"])
    min_inferior, min_superior = get_tukey_limits(daily_max_min["min"])
    return max_inferior, max_superior, min_inferior, min_superior


def get_tukey_fences_by_daily_means(data_copy, column_name):
    daily_means = get_daily_mean(data_copy, column_name)
    linf, lsup = get_tukey_limits(daily_means)
    return linf, lsup


def get_outliers(Variable, inferior_limit, superior_limit) -> list[Any]:
    outliers = [x for x in Variable if x < inferior_limit or x > superior_limit]
    return outliers


def get_tukey_limits(Variable):
    Q1 = np.nanpercentile(Variable, 25)
    Q3 = np.nanpercentile(Variable, 75)
    IQR = Q3 - Q1
    linf = Q1 - 1.5 * IQR
    lsup = Q3 + 1.5 * IQR
    return linf, lsup
