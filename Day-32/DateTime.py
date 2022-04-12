import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

month = now.month
print(month)

day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2000, month=11, day=12, hour=3)
print(date_of_birth)