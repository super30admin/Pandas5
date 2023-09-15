'''
Return the Index label if some condition is satisfied over a column in Pandas Dataframe
1. Using index.list
2. df.query()
'''

import pandas as pd

df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
				'Product':['Umbrella', 'Mattress', 'Badminton', 'Shuttle'],
				'Last_Price':[1200, 1500, 1600, 352],
				'Updated_Price':[1250, 1450, 1550, 400],
				'Discount':[10, 10, 10, 10]})

# Create indexes
df.index =['Item 1', 'Item 2', 'Item 3', 'Item 4']
print(df)

# 1. Using index & to_list
filtered_indices = df[df['Updated_Price']>1000].index.to_list()
print(filtered_indices)

# 2. Using df.query
filtered_indices = df.query('Updated_Price < 500').index.to_list()
print(filtered_indices)