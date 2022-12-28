# Write your solution in this file

f = open("output.txt", 'w')
for count in range(0, 10001):
    d = str(count).rjust(10)
    b = str(bin(count)).rjust(20)
    h = str(hex(count)).rjust(10)


    f.write("".join([d, b, h]) + "\n")

f.close()
