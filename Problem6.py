'''
1. Using dt.to_period function to calculate diff in Monthends 
2. Calculate Timedelta using months in integer
3. Using a custom function
'''

import pandas as pd

data = pd.read_csv('time.csv')

# converting columns to datetime
data['start_date'] = pd.to_datetime(data['start_date'])
data['end_date'] = pd.to_datetime(data['end_date'])

# calculating time delta in monthends
data['time_delta_months'] = data['end_date'].dt.to_period('M') - \
	data['start_date'].dt.to_period('M')

# Monthends object is returned
print(data)

# 2a. calculating time delta in integer months using astype on Monthends
data['time_delta_months'] = data['end_date'].dt.to_period('M').astype(int) - \
	data['start_date'].dt.to_period('M').astype(int)
print(data)


# 2b. calculating time delta in integer months using view on Monthends
data['time_delta_months'] = data['end_date'].dt.to_period('M').view(dtype='int64') - \
	data['start_date'].dt.to_period('M').view(dtype='int64')
print(data)

# 3.  Using custom function 
data = pd.DataFrame({'startdate': [pd.Timestamp('20181211'),
								pd.Timestamp('20180701')],
					'enddate': [pd.Timestamp('20190612'),
								pd.Timestamp('20190712')]})

def time_delta_month(end, start):
	return 12 * (end.dt.year - start.dt.year) \
		+ (end.dt.month - start.dt.month)

print(time_delta_month(data['enddate'], data['startdate']))
