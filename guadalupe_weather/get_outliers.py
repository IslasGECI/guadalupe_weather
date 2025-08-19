import numpy as np


def remove_outliers(Variable):
    outliers = get_outliers(Variable)
    return Variable.replace(outliers, np.nan)


def get_outliers(Variable):
    Q1 = np.percentile(Variable, 25)
    Q3 = np.percentile(Variable, 75)
    IQR = Q3 - Q1
    linf = Q1 - 1.5 * IQR
    lsup = Q3 + 1.5 * IQR

    outliers = [x for x in Variable if x < linf or x > lsup]
    return outliers
