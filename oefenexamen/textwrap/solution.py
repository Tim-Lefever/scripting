# Write your solution in this file
import re


with open("input.txt") as file:
    with open("output.txt", 'w') as output:
        for str in file:
            output.write('\n'.join(line.strip() for line in re.findall(r'.{1,40}(?:\s+|$)', str)))


    
