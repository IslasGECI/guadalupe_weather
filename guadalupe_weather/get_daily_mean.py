def get_daily_max_and_min(data, column_name):
    return data.groupby(["Date"])[column_name].agg(["min", "max"]).reset_index()


def get_daily_mean(data, variable):
    return data.groupby(["Date"])[variable].mean()
