import pandas as pd
import numpy as np

df = pd.read_csv('telecom_churn.csv')

df1 = df.groupby(['State']).agg({'Total day calls': 'mean'})

df2 = df1[df1['Total day calls'] >df['Total day calls'].mean()]

print(df2)
