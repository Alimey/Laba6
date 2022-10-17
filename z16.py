import pandas as pd

df = pd.read_csv('telecom_churn.csv')

df1 = df.groupby(['State']).agg({'Total day charge' : 'mean'})
df2 = df1.sort_values(by='Total day charge')
print(df2)