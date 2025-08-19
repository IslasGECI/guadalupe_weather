from guadalupe_weather.get_outliers import get_outliers, remove_outliers
import pandas as pd
import numpy as np

outlier = 50
data = pd.DataFrame({"Variable": [2, 3, 5, 7, 9, 11, 14, 18, 22, outlier]})


def test_get_outliers():
    obtained = get_outliers(data.Variable)
    assert obtained == [outlier]


def tests_remove_outliers():
    obtained = remove_outliers(data.Variable)
    assert len(obtained) == len(data)
    assert np.isnan(obtained.iloc[-1])
