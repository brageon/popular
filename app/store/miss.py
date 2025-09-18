import pandas as pd
import numpy as np
df = pd.read_csv('andro.csv')
n_missings_each_col = df.apply(lambda x: x.isnull().sum())
print(n_missings_each_col.argmax())
print(df.loc[df.isnull().any(axis=1)])