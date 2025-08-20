import numpy as np
from pyparsing import Any


def remove_outliers_for_column(data, column_name):
    data_copy = data.copy()
    column_data = data[column_name]
    outliers = get_outliers(column_data)
    data_copy[column_name] = column_data.replace(outliers, np.nan)
    return data_copy


def get_outliers(Variable) -> list[Any]:
    linf, lsup = get_tukey_limits(Variable)
    return xxget_outliers(Variable, linf, lsup)


def xxget_outliers(Variable, inferior_limit, superior_limit) -> list[Any]:
    outliers = [x for x in Variable if x < inferior_limit or x > superior_limit]
    return outliers


def get_tukey_limits(Variable):
    Q1 = np.nanpercentile(Variable, 25)
    Q3 = np.nanpercentile(Variable, 75)
    IQR = Q3 - Q1
    linf = Q1 - 1.5 * IQR
    lsup = Q3 + 1.5 * IQR
    return linf, lsup
