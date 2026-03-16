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

#using csv.DictWriter method
import csv
data = [
    {'Name': 'John','Age': 20, 'City': 'Hyderabad'},
    {'Name': 'Sreekanth','Age': 21, 'City': 'Pune'},
    {'Name': 'Lucy','Age': 40, 'City': 'New York'}
]
with open('dictwriter-example.csv','w',newline = '') as file:
    writer = csv.DictWriter(file,fieldnames=['Name','Age','City'])
    writer.writeheader()
    writer.writerows(data)

#using csv.writer() method
import csv
rows=[
    ['Name','Age','City'],
    ['Rohan',22,'New Delhi'],
    ['Abhay',23,'Noida'],
    ['Vivek',24,'Gurgaon']
]
with open('writer-output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
with open('writer-output.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#Custom delimeter
import csv
data = [
    ['Product','Price', 'Stock'],
    ['Pen',2.5, 100],
    ['Notebook',3.0, 50]
]
with open('semicolon-output.csv','w', newline='') as file:
    writer = csv.writer(file, delimiter= ';')
    writer.writerows(data)



#Quote fields
import csv
data = [
    ['Name','Comment'],
    ['Abhay', 'Hello Sir, the work is done"'],
    ['Vivek','Great Work']
]
with open ('quoted-output.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting= csv.QUOTE_ALL)
    writer.writerows(data)
print("CSV file 'quoted-output.csv' created successfully!")

with open('quoted-output.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#Handling missing files
import csv
data = [
    {'Name': 'Lucy', 'Age':30},
    {'Name': 'Peter', 'Age':25, 'City': 'Miami'}
]
with open('dict-missing-fields.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file,fieldnames = ['Name','Age', 'City'], restval = 'N/A')
    writer.writeheader()
    writer.writerows(data)