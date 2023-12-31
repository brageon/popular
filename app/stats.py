import numpy as np
import pandas as pd
df=pd.read_csv('Casual.csv')
df.loc[df.score == np.max(df.score)]
row,col=np.where(df.values == np.max(df.score))
ab=df.iloc[row[0]], col[0]
df.to_csv('Cas.csv')
'''
# df = pd.read_fwf('dif.txt')
# df.to_csv('dif.csv')
df = pd.read_csv('dif.csv')
ab = df.reviews.min('Tools')
ac = df.reviews.max('Casual')
ad = df.reviews.median('Arcade')
print(ab,ac,ad)
'''
