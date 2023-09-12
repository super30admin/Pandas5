# How to Calculate Timedelta in Months in Pandas 

import pandas as pd

# reading the csv file
data = pd.read_csv('time.csv')

# converting columns to datetime
data['start_date'] = pd.to_datetime(data['start_date'])
data['end_date'] = pd.to_datetime(data['end_date'])

# calculating time delta in months
data['time_delta_months'] = data['end_date'].dt.to_period('M') - \
	data['start_date'].dt.to_period('M')
print(data)

# Method 2- Calculate Timedelta using months in integer


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# converting columns to datetime
data['start_date'] = pd.to_datetime(data['start_date'])
data['end_date'] = pd.to_datetime(data['end_date'])

# calculating time delta in months
data['time_delta_months'] = data['end_date'].dt.to_period('M').astype(int) - \
	data['start_date'].dt.to_period('M').astype(int)

print(data)
