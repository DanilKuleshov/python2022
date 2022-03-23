Lines = []
with open('input.txt', 'r') as Input:
    line = Input.readlines()
    line = str(line)[2:-2]
    Lines.append([0, 0])
    y = 0
    x = 0
    for i in line:

        if i == '>':
            x += 1
        elif i == '<':
            x += -1
        elif i == '^':
            y += 1
        elif i == 'v':
            y += -1
        else:
            print('Something is wrong.')

        Lines.append([x, y])
    array1 = Lines.copy()
    for j in array1:
        if Lines.count(j) > 1:
            for k in range(Lines.count(j) - 1):
                Lines.remove(j)
print('Санта посетил ' + str(len(Lines)) + ' дома за ночь!')

with open('output1.txt', 'w') as output:
    output.write(str(len(Lines)))