import numpy as np
import pandas as pd
import sys, csv
file1 = input("Enter file: ") 
if file1.endswith("csv"):
    print("Grattis!")
else:
    exit()
df=pd.read_csv(file1, on_bad_lines='skip')
for col in df.columns:
    print(col, end=' ')
file2 = input("\n" + "Enter col: ")
e = int(input("Enter need as neg: "))
df.drop(df.columns[1],axis=1,inplace=True)
for col in df.columns:           
    print(str(df.columns.get_loc(col)) + '\t' + col)
ab=df[file2].value_counts()
print(ab,len(ab))
with open(file1, 'r') as xarx:
    reader = csv.DictReader(xarx)
    highest = sorted(reader, key=lambda x: x[file2])[e:]
ew=pd.DataFrame(highest)
file3 = input("Enter filename to save: ")
ew.to_csv(file3, mode='a')
with open(file3, 'r') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
def get_total(row):
    total = 0
    for key, value in row.items():
        if key not in ['app_id', 'title', 'released', 'genre', 'genre_id', 'offers_iap', 'ad_supported']:
            total += float(value)
    return total
for i, row in enumerate(rows):
    total = int(get_total(row))
    print("Row", i+1, "total value:", total)
highest_indexes = []
for i in range(len(rows)): 
    for j in range(i+1, len(rows)): 
        total_i = get_total(rows[i]) 
        total_j = get_total(rows[j]) 
        if total_i > total_j: 
            highest_indexes.append(i) 
        elif total_i < total_j: 
            highest_indexes.append(j) 
        else: 
            pass
si = sorted(highest_indexes, reverse=True)[:1] 
print("Row index:", si)
'''
list_of_names = list(df.columns)
total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print("Number of Rows: "+str(total_rows))
print("Number of Columns: "+str(total_cols))
print("List of column names : ",
      list_of_names[0])
      
df = pd.read_csv('andro.csv')
n_missings_each_col = df.apply(lambda x: x.isnull().sum())
print(n_missings_each_col.argmax())
print(df.loc[df.isnull().any(axis=1)])