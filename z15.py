import pandas as pd

df = pd.read_csv('telecom_churn.csv')

mean_loyal = df[df['Churn'] == False]['Total day charge'].mean()
mean_unloyal = df[df['Churn'] == True]['Total day charge'].mean()

if mean_loyal>mean_unloyal:
    print('mean_loyal_charge > mean_unloyal_charge')
elif mean_unloyal == mean_loyal:
    print('the same')
else:
    print('mean_loyal_charge < mean_unloyal_charge')
