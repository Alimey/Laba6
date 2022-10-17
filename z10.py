import pandas as pd

df = pd.read_csv('telecom_churn.csv')

n = len(df['Area code'].unique())

print(n)