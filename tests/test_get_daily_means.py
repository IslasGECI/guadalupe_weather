from guadalupe_weather.get_daily_mean import get_daily_mean
import pandas as pd


def test_get_daily_mean():
    data = pd.DataFrame(
        {
            "Date": ["30/Sep/2008", "30/Sep/2008", "01/Oct/2008", "01/Oct/2008", "01/Oct/2008"],
            "Time": ["03:00:00", "04:00:00", "11:00:00", "12:00:00", "13:00:00"],
            "Temp_Out": [19.2, 20.1, 21.5, 19.8, 18.7],
        }
    )
    obtained = get_daily_mean(data)
    assert len(obtained) == 2
