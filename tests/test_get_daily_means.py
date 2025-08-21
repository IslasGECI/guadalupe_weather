from guadalupe_weather.get_daily_mean import get_daily_mean, get_daily_max_and_min
import pandas as pd


def test_get_daily_mean():
    data = pd.DataFrame(
        {
            "Date": ["30/Sep/2008", "30/Sep/2008", "01/Oct/2008", "01/Oct/2008", "01/Oct/2008"],
            "Time": ["03:00:00", "04:00:00", "11:00:00", "12:00:00", "13:00:00"],
            "Temp_Out": [19.2, 20.1, 21.5, 19.8, 18.7],
            "Rain_Rate": [2, 2, 2, 2, 2],
        }
    )
    obtained = get_daily_mean(data, "Temp_Out")
    assert len(obtained) == 2
    obtained = get_daily_mean(data, "Rain_Rate")
    assert obtained.iloc[0] == 2
    obtained = get_daily_max_and_min(data, "Temp_Out")
    assert obtained.shape == (2, 3)
