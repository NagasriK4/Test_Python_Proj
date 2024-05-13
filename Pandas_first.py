import pandas as pd
data = { 'Name' : ['Avnika','Nainika'],
         'Age' : [5,1],
         'City' : ['Brampton','Brampton']}
df = pd.DataFrame(data)
print(df['Name'])
print(df)