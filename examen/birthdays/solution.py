# Write your solution in this file
'''open data.json'''
import json

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

'''for each person in data, print their name and their birthday'''
counts = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
for person in data:
    month = person['birthday']['month']
    counts[str(month)] += 1


year = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
for month, count in counts.items():
    stars = '*' * count
    print(f'{year[month].rjust(10)} {stars}')

'''write the output to a file'''
with open('output.txt', 'w') as f:
    for month, count in counts.items():
        stars = '*' * count
        f.write(f'{year[month].rjust(10)} {stars}\n')

print(counts['1'])

