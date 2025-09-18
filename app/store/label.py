import pandas as pd
df=pd.read_csv('andro.csv', on_bad_lines='skip')
#df.pop(['title', 'genre_id', 'price', 'rating_one_star', 'rating_two_star', 'rating_three_star', 'rating_four_star'])
df.drop(df.columns[1],axis=1,inplace=True)
for col in df.columns:           
    print(str(df.columns.get_loc(col)) + '\t' + col)
ab=df['genre'].unique()
print(ab)