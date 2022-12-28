# Write your solution in this file
import csv
'''open violations.csv'''

"""calculate fine by speed"""
def calculate_fine(speed):
    return int(speed) - 120

fines = {}


with open('violations.csv', encoding='utf-8') as f:
    '''csv reader'''
    reader = csv.DictReader(f)
    for row in reader:
        license = row['license_plate']
        # print(license)
        if license not in fines:
            fines[license] = 0
        fines[license] += int(calculate_fine(row['speed']))

'''get sorted list on fines, then by plate'''
sorted_fines = sorted(fines.items(), key=lambda x: x[0])
sorted_fines = sorted(sorted_fines, key=lambda x: x[1])

with open('output.txt', 'w', encoding='utf-8') as out:
    for plate, fine in sorted_fines:
        out.write(f'{plate} {fine}\n')

print(fines)