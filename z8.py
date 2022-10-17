import pandas as pd

df = pd.read_csv('telecom_churn.csv')

df1 = df.groupby(['State']).agg({'Total day calls': 'mean', 'Total eve calls': 'mean'})
df1["Answer"] = df1['Total day calls']>df1['Total eve calls']

print(df1)