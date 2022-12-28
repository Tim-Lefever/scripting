# Write your solution in this file
from encodings import utf_8
from itertools import count
import sys, csv


def remove_n(name):
    return name.replace("\n", "")

data = []

with open("input.txt", encoding="utf_8") as file:
    data = file.readlines()
    file.close()



score = {}

for race in range(100):
    for competetor in range(100):
        name = data[(race) * 100 + competetor]
        if name not in score:
            score[name] = 0
        score[name] += 100 - competetor

ranking = [(name, score[name]) for name in score]
ranking.sort(key= lambda x: x[1], reverse=True)


f = open("output.txt", "w")
for pair in ranking[:10]:
    f.write(remove_n(pair[0]) + "\n")
f.close()



