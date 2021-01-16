import os
import csv
records_folder = 'Transactions'
mainpath = os.listdir(records_folder)
path_to_csv = mainpath[0]
reader = csv.reader(open(f"{records_folder}/{path_to_csv}", 'r'))
for row in reader:
    print(row)