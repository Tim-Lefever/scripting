import argparse
from itertools import count
import math

def mult(xs):
    if len(xs) == 0:
        return None
    if len(xs) == 1:
        return xs[0]
    else:
        first = xs[0]
        rest = xs[1:]
        return first * mult(rest)

def dict_to_string(dict):
    arr = []
    for key in dict:
        if key != -1:
            arr.append(str(key) + "^" + str(dict[key]))
        else:
            arr.append(str(key))
    return " * ".join(arr)


parser = argparse.ArgumentParser()
parser.add_argument("number", nargs=1, type=int)

args = parser.parse_args()
num = args.number[0]

factors = []
if num < 0:
    factors.append(-1)
    num *= -1
if num == 0:
    factors.append(0)

# sqrt = int(math.ceil(math.sqrt(num)))
for i in range(2, num):
    if num == 1:
            break
    while 1:
        if num % i == 0:
            # print(num, i)
            factors.append(i)
            num /= i
        else:
            break

counts = {}
for int in factors:
    if int not in counts:
        counts[int] = 0
    counts[int] += 1

print(str(mult(factors)) + " = " + dict_to_string(counts))