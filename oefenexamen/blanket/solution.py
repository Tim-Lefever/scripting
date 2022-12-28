from encodings import utf_8
import sys, csv, json, math, datetime
import datetime
from statistics import mean
# Write your solution in this file

dict = {}

with open("input.txt") as file:
    dict = json.load(file)


array = [[date, round(sum(dict[date])/len(dict[date]))] for date in dict]


array.sort(key=lambda x: datetime.datetime.strptime(x[0], '%d/%m/%Y'))
print(array)

f = open("output.txt", 'w')
for date in array:
    f.write(str(date[1]) + "\n")