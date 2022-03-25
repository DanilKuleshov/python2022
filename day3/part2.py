Lines = []
with open('input.txt', 'r') as INPUT:
    line = INPUT.readlines()
    line = str(line)[2:-2]

    Lines.append([0,0])
    y=0
    x=0
    l = 0
    for i in line:
        l += 1
        if l % 2 == 0:
            continue
        elif i == '>':
            x += 1
        elif i == '<':
            x += -1
        elif i == '^':
            y += 1
        elif i == 'v':
            y += -1
        Lines.append([x,y])
    a=0
    b=0
    l=0
    for i in line:
        l += 1
        if l % 2 != 0:
            continue
        elif i == '>':
            a += 1
        elif i == '<':
            a += -1
        elif i == '^':
            b += 1
        elif i == 'v':
            b += -1
        Lines.append([a,b])
    array1 = Lines.copy()
    for j in array1:
        if Lines.count(j) > 1:
            for k in range(Lines.count(j) - 1):
                Lines.remove(j)
    print('Домов, получивших хотябы один подарок ', str(len(Lines)))
INPUT.close()
with open('output2.txt','w') as output:
    output.write(str(len(Lines)))