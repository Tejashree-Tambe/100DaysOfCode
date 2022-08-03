import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

dob = dt.datetime(year=2001, month=1, day=5)
print(dob)
