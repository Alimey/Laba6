import pandas as pd

df = pd.read_csv('telecom_churn.csv')
# print(df.columns)
# print('-----------------------------------------------------------------------------')
print('Среднее количество звонков: ', df['Total day calls'].mean())