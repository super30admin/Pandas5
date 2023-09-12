# Python3 code to demonstrate working of Business days in range



from datetime import datetime,timedelta

test_date1,test_date2=datetime(2015,6,3),datetime(2015,7,1)

dates=(test_date1+timedelta(idx+1)
       for idx in range((test_date2-test_date1).days))

result=sum(1 for day in dates if day.weekday()<5)

print("Total business days in range:"+str(result))


# Python3 code to demonstrate working of Business days in range
# Using pd.bdate_range
from datetime import datetime
import pandas as pd


test_date1, test_date2 = datetime(2015, 6, 3), datetime(2015, 6, 30)

# generating total days using pd.bdate_range()
# len() gets the number of days
# includes both last and first date.
res = len(pd.bdate_range(test_date1.strftime('%Y-%m-%d'),
						test_date2.strftime('%Y-%m-%d')))

print("Total business days in range : " + str(res))
