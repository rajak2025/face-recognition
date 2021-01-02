#import pandas as pd
#df = pd.read_csv('face-recognition/transactions.csv', engine='python',header=0)

#print(df)
#print(type(df))

import csv
reader = csv.reader(open('face-recognition/transactions.csv', 'r'))
d = {}
for row in reader:
   name, phone, date, items = row
   d[name] = phone, date, items

value_list = d['Alex']

print(value_list[0])