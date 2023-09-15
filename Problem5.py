'''
Computing the difference in dates in
1. No of months
2. No of days
3. No of weeks
4. No of years
'''
import pandas as pd
import numpy as np
import datetime

df = pd.DataFrame({'dates1': np.array(
[datetime.datetime(2000, 10, 19), datetime.datetime(2021, 1, 8)]),
				'dates2': np.array(
					[datetime.datetime(1998, 6, 20),
					datetime.datetime(2012, 10, 18)])})

# 1. Used to convert the difference in terms of months
df['Number_of_months'] = ((df.dates1 - df.dates2)/np.timedelta64(1, 'M'))
df['Number_of_months'] = df['Number_of_months'].astype(int)
print(df)

# 2 No. of days
df['Number_of_days'] = ((df.dates1 - df.dates2)/np.timedelta64(1, 'D'))
df['Number_of_days'] = df['Number_of_days'].astype(int)

# 3. No. of weeks
df['Number_of_weeks'] = ((df.dates1 - df.dates2)/np.timedelta64(1, 'W'))
df['Number_of_weeks'] = df['Number_of_weeks'].astype(int)

# 4. No. of years
df['Number_of_years'] = ((df.dates1 - df.dates2)/np.timedelta64(1, 'Y'))
df['Number_of_years'] = df['Number_of_years'].astype(int)
print(df)