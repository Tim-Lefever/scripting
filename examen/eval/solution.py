# Write your solution in this file


'''open input.txt'''
import re

def calculate(match):
    op = match.group(2)
    print(op)
    first = int(match.group(1).strip())
    second = int(match.group(3).strip())
    print(first, second, op)
    if op == '+':
        return str(int(first + second))
    if op == '*':
        return str(int(first * second))
    return None
    

with open('output.txt', 'w', encoding='utf-8') as out:
    with open('input.txt', encoding='utf-8') as f:
        for line in f:
            line = re.sub(r'\$\{([ 0-9]*)([\+|\*])([ 0-9]*)\}\$?', calculate, line)
            print(line)
            '''print line to output.txt'''
            out.write(line)

