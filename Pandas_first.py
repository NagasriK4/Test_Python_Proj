import pandas as pd
data1 = { 'Name' : ['Avnika','Nainika'],
         'Age' : [5,1],
         'City' : ['Brampton','Brampton']}
df = pd.DataFrame(data1)
print(df['Name'])
print(df)