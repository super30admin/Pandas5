# Problem 5 Pandas – Number of Months Between Two Dates

import pandas as pd
import numpy as np
import datetime

# Making a dataframe which will have two columns two store different dates

df=pd.DataFrame({'dates1':np.array([datetime.datetime(2000,10,19),datetime.datetime(2021,1,8)]),
                 'dates2':np.array([datetime.datetime(1998,6,20),datetime.datetime(2012,10,18)])})
print(df)

#  Used to convert the difference in terms of months

df['nb_months']=((df.dates1-df.dates2)/np.timedelta64(1,'M'))
df['nb_months']=df['nb_months'].astype(int)
print(df)