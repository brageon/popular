# https://willkoehrsen.github.io/machine%20learning/python/project/machine-learning-with-python-on-the-enron-dataset/
from sklearn.preprocessing import Imputer
import pandas as pd
df = pd.DataFrame()
df[payment_data] = df[payment_data].fillna(0)
df[stock_data] = df[stock_data].fillna(0)
imp = Imputer(missing_values='NaN', strategy = 'mean', axis=0)
df_poi = df[df['poi'] == True];
df_nonpoi = df[df['poi']==False]
df_poi.ix[:, email_data] = imp.fit_transform(df_poi.ix[:,email_data]);
df_nonpoi.ix[:, email_data] = imp.fit_transform(df_nonpoi.ix[:,email_data]);
df = df_poi.append(df_nonpoi)
errors = (df[df[payment_data[:-1]].sum(axis='columns') != df['total_payments']])
ab = len(df[df[stock_data[:-1]].sum(axis='columns') != df['total_stock_value']])
print(errors)
print(ab)
IQR = df.quantile(q=0.75) - df.quantile(q=0.25)
first_quartile = df.quantile(q=0.25)
third_quartile = df.quantile(q=0.75)
outliers = df[(df>(third_quartile + 1.5*IQR) ) | (df<(first_quartile - 1.5*IQR) )].count(axis=1)
outliers.sort_values(axis=0, ascending=False, inplace=True)
outliers.head(12)
df.drop(axis=0, labels=['FREVERT MARK A', 'LAVORATO JOHN J', 'WHALLEY LAWRENCE G', 'BAXTER JOHN C'], inplace=True)
df['poi'].value_counts()
