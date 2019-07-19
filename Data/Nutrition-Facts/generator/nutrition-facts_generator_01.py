# import csv

# with open('Nutrition-Facts.csv', encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile) # read rows into a dictionary format
#     for row in reader:
#         print(row['Nutrition Facts'])
#         print(row[0])

import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('Nutrition-Facts.csv', encoding="utf-8") as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
            print(row.items())