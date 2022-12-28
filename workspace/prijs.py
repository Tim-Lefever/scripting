from tkinter.tix import INTEGER


rangeInt = 101
n = 5
a = 2.65
b = 1.80


for x in range(rangeInt):
    for y in range(rangeInt):
        if (a * x + b * y) % n == 0:
            print (x, y, a *x + b * y)
        
