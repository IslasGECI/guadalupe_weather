from guadalupe_weather.get_outliers import get_outliers
import pandas as pd

data = pd.DataFrame({"Variable": [2, 3, 5, 7, 9, 11, 14, 18, 22, 50]})


def test_get_outliers():
    obtained = get_outliers(data.Variable)
