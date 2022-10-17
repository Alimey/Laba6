import pandas as pd

df = pd.read_csv('telecom_churn.csv')

df1 = df.groupby(['Customer service calls']).count().State

print(df1)