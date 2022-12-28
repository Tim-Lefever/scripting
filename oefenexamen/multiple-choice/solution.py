# Write your solution in this file
from codecs import utf_16_be_decode
import csv, sys
from encodings import utf_8


def remove_n(str):
    return str.replace("\n", "")

# get solution
solution = []
with open("solutions.csv", encoding="utf_8") as file:
    solution = file.readline().split(",")

print(solution)

f = open("output.txt", 'w')

with open("answers.csv", encoding="utf_8") as file:
    for line in file:
        answers = line.split(",")
        name = answers.pop(0)
        # print(name, answers)
        score = 0
        for question in range(len(solution)):
            if (solution[question] == answers[question]):
                score += 1
        f.write(" ".join([name, str(score)]) + "\n")


        