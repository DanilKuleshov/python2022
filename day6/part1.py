lights = []
for y in range(1000):
    for x in range(1000):
        lights.append([x, y, 0])

with open('input.txt', 'r') as INPUT:
    for line in INPUT:

        if '\n' in line:
            line = line[0:-1]
        line = line.split(' ')

        if line[0] == 'turn':
            if line[1] == 'on':
                start_coord = str(line[2]).split(',')
                end_coord = str(line[4]).split(',')
                for y in range(int(start_coord[1]), int(end_coord[1]) + 1):
                    for x in range(int(start_coord[0]), int(end_coord[0]) + 1):
                        lights[1000 * y + x][2] = 1
            elif line[1] == 'off':
                start_coord = str(line[2]).split(',')
                end_coord = str(line[4]).split(',')
                for y in range(int(start_coord[1]), int(end_coord[1]) + 1):
                    for x in range(int(start_coord[0]), int(end_coord[0]) + 1):
                        lights[1000 * y + x][2] = 0


        elif line[0] == 'toggle':
            start_coord = str(line[1]).split(',')
            end_coord = str(line[3]).split(',')
            for y in range(int(start_coord[1]), int(end_coord[1]) + 1):
                for x in range(int(start_coord[0]), int(end_coord[0]) + 1):
                    if lights[1000 * y + x][2] == 1:
                        lights[1000 * y + x][2] = 0
                    elif lights[1000 * y + x][2] == 0:
                        lights[1000 * y + x][2] = 1

resoult = 0
for element in lights:
    if element[2] == 1:
        resoult += 1

with open('output1.txt', 'w') as OUTPUT:
    OUTPUT.write(str(resoult))
print(resoult)