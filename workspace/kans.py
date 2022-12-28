import itertools


def generate(string):
    '''list of all letters in string'''
    letters = list(string)
    return set(''.join(comb) for comb in list(itertools.permutations(letters)))

all = generate('0123456789')
good = set()
for comb in all:
    if comb.index('0') < comb.index('9') and comb.index('0') < comb.index('8'):
        good.add(comb)
        # print('found:', comb)

print(str(len(good)) + "/" + str(len(all)) + '=' + str(len(good) / len(all)))
print("10*9*8*7*6*5*4*2*1 ="  + str(10 * 9 * 8 * 7 * 6 * 5 * 4 * 2 * 1))