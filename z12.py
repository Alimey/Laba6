import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('telecom_churn.csv')

df0 = df[df['Churn'] == True]

df1 = df0.groupby(['Customer service calls']).count()
df2 = df.groupby(['Customer service calls']).count()

df3 = df1['State']/df2['State']

print(df3)

plt.plot(df3)
plt.show()
