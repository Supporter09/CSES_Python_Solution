import datetime
def add_days(cur_date, n):
    res = cur_date + datetime.timedelta(days=n)
    return res
cur_date = datetime.date(2016,2,10)
print(add_days(cur_date, 30))