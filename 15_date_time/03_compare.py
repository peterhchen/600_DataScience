import datetime
today_date = datetime.date.today()
print('today_date:', today_date)
# create delta days
delta_days = datetime.timedelta (days=4)
print ('delta_days:', delta_days)
before_four_days = today_date - delta_days
print('before_four_days', before_four_days)
after_four_days = today_date + delta_days
print('after_four_days', after_four_days)
if before_four_days < after_four_days:
    print ('before_four_days < after_four_days')
if before_four_days < today_date:
    print ('before_four_days < today_date')
if after_four_days > today_date:
    print ('after_four_days > today_datee')