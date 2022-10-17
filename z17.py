import pandas as pd

df = pd.read_csv('telecom_churn.csv')

df1 = df.groupby(['Area code']).mean()

print(df1)