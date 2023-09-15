'''
1. Using timedelta(), sum(), weekday()
2. Using np.busday_count()
3. Using pandas.bdate_range()
4. Using loop and weekday
5. Using numpy
'''

from datetime import datetime, timedelta
import numpy as np
import pandas as pd

test_date1, test_date2 = datetime(2015, 6, 3), datetime(2015, 7, 1)
print("The original range : " + str(test_date1) + " " + str(test_date2))


dates = (test_date1 + timedelta(idx + 1) 
         for idx in range((test_date2 - test_date1).days))

# 1. Using timedelta, weekday,sum
res = sum(1 for day in dates if day.weekday() < 5)
print("Total business days in range : " + str(res))

# 2. Using np.busyday_count()
res = np.busday_count(test_date1.strftime('%Y-%m-%d'),
                      test_date2.strftime('%Y-%m-%d'))
print("Total business days in range : " + str(res))

# 3. Using pandas bdate_range()
# inclusive{“both”, “neither”, “left”, “right”}, default “both” parameter
res = len(pd.bdate_range(test_date1.strftime('%Y-%m-%d'),
                         test_date2.strftime('%Y-%m-%d')))
print("Total business days in range : " + str(res))

# 4. Using a loop and weekday()
num_business_days = 0

current_date = test_date1
while current_date < test_date2:
	if current_date.weekday() < 5:
		num_business_days += 1
	current_date += timedelta(days=1)

print("Total business days in range:", num_business_days)

# 5. Using numpy
# creating an array of dates between the start and end dates
dates = np.arange(test_date1, test_date2 + timedelta(days=1), dtype='datetime64[D]')
 
# getting the weekday number for each date in the array
weekday_num = np.datetime_as_string(dates, unit='D').astype('datetime64[D]').view('int') % 7
 
# counting the number of weekdays in the array using a condition
num_business_days = np.count_nonzero((weekday_num < 5))
 
print("Total business days in range:", num_business_days)
