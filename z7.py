import pandas as pd

df = pd.read_csv('telecom_churn.csv')

df1 = df.groupby(['State']).agg({'Total day calls': 'mean', 'Total eve calls': 'mean'})
print(df1)