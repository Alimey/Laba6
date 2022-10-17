import pandas as pd
import numpy as np

A = np.random.randint(-10, 10, 10)
B = np.random.randint(-10, 10, 10)

df = pd.DataFrame({'A': A, 'B': B})

A1 = np.array([a*a for a in A])
B1 = np.array([b*b for b in B])

A_B = A1+B1

df['A^2 + B^2'] = A_B

# Округлила до 2 цифр после запятой, чтобы выглядело аккуратней
df['mean'] = round(df.mean(axis=1), 2)

print(df)