"""
#using csv.reader() method
import csv
with open('companies.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#using csv.DictRead() method
import csv 
with open('companies.csv', newline= '') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

import pandas as pd
dframe = pd.read_csv('companies.csv')
print(dframe)
"""