import pandas as pd

df = pd.read_csv('telecom_churn.csv')

print(df.groupby(['State']).agg({'Total day calls': 'mean'}).loc["CA"])