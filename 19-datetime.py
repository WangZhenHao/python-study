import datetime

date = datetime.date(2019, 1, 1)
today = datetime.date.today()

# print(today)

now = datetime.datetime.now()

now = now.strftime("%Y-%m-%d %H:%M:%S")

# print(now)


target_datetime = datetime.datetime(2026, 1, 1, 10, 10, 1)
print(target_datetime)