import numpy as np


def remove_outliers_for_column(data, column_name):
    data_copy = data.copy()
    column_data = data[column_name]
    outliers = get_outliers(column_data)
    data_copy[column_name] = column_data.replace(outliers, np.nan)
    return data_copy


def get_outliers(Variable):
    Q1 = np.percentile(Variable, 25)
    Q3 = np.percentile(Variable, 75)
    IQR = Q3 - Q1
    linf = Q1 - 1.5 * IQR
    lsup = Q3 + 1.5 * IQR

    outliers = [x for x in Variable if x < linf or x > lsup]
    return outliers
