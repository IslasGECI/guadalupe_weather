def get_daily_mean(data):
    return data.groupby(["Date"])["Temp_Out"].mean()
