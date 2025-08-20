from guadalupe_weather.get_outliers import get_outliers, remove_outliers_for_column
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
