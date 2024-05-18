import matplotlib.pyplot as plt
import pandas as pd
import csv, numpy 
# df = pd.read_fwf('../prep/dif.txt')
# df.to_csv('../prep/dif.csv')
df = pd.read_csv('../prep/dif.csv')
ab = df.reviews.min('Tools')
ac = df.reviews.max('Casual')
ad = df.reviews.median('Arcade')
print(ab,ac,ad)
'''
# tor = db.mean()
# tor.to_csv('Ove.csv', mode='a')
Subjects = []
Scores = []
  
with open('../andro.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
        Subjects.append(row[1])
        Scores.append(int(row[2]))
  
plt.pie(Scores,labels = Subjects,autopct = '%.2f%%')
plt.title('Marks of a Student', fontsize = 20)
plt.show()
'''