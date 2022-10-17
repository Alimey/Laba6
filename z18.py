import pandas as pd

df = pd.read_csv('telecom_churn.csv')

df1 = df[['State', 'Churn']].iloc[[100-1, 102-1, 104-1]]

print(df1)