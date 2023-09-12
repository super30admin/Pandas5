# Problem 2 :Using dictionary to remap values in Pandas DataFrame columns


import pandas as pd
df = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
				'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
				'Cost': [10000, 5000, 15000, 2000]})


# Remap values in Pandas columns using replace() function

# Create a dictionary using which we
# will remap the values
dict = {'Music' : 'M', 'Poetry' : 'P', 'Theatre' : 'T', 'Comedy' : 'C'}

# Remap the values of the dataframe
df1=df.replace({"Event": dict})


print(df1)

# Remap values in Pandas DataFrame columns using map() function
df['Event']=df['Event'].map(dict)
print(df)

