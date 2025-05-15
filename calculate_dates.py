runweeks = [0,1,2,3]

import datetime

def getdates():
    basedate = datetime.date(2025, 2, 20)

    dates = []

    for week in runweeks:
        for day in range(5):
            date = basedate + datetime.timedelta(weeks= week, days=day)
            dates.append([date.year, date.month, date.day])
    return dates