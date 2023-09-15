'''
Using dictionary to remap values in Pandas DataFrame columns
1. Using replace function
2. Using map function
'''

import pandas as pd

df = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
				'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
				'Cost': [10000, 5000, 15000, 2000]})

print(df)

dict = {'Music' : 'M', 'Poetry' : 'P', 'Theatre' : 'T', 'Comedy' : 'C'}

# Using replace function
df1 = df.replace({'Event':dict})
print(df1)

# Using map function
df2 = df['Event'].map(dict)
print(df2)


