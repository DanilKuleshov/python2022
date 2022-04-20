from itertools import groupby
INPUT = open('input.txt', 'r'). read()
file = open('output2.txt', 'w+')
for i in range(50):
    INPUT = ''.join([str(len(list(g)))+k for k, g in groupby(INPUT)])
file.write(str(len(INPUT)))
file.close()