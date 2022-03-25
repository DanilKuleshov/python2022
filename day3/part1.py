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
        Lines.append([x, y])
    counts = Lines.copy()
    for j in counts:
        if Lines.count(j) > 1:
            for k in range(Lines.count(j) - 1):
                Lines.remove(j)
print('Домов, получивших хотябы один подарок ', str(len(Lines)))

with open('output1.txt', 'w') as output:
    output.write(str(len(Lines)))
