lights = []
for y in range(1000):
    for x in range(1000):
        lights.append([x, y, 0])

with open('input.txt', 'r') as INPUT:
    for line in INPUT:

        text = line
        if '\n' in text:
            text = text[0:-1]
        text = text.split(' ')

        if text[0] == 'turn':

            # on
            if text[1] == 'on':
                start_coord = str(text[2]).split(',')
                end_coord = str(text[4]).split(',')
                for y in range(int(start_coord[1]), int(end_coord[1]) + 1):
                    for x in range(int(start_coord[0]), int(end_coord[0]) + 1):
                        lights[1000 * y + x][2] += 1

            # off
            elif text[1] == 'off':
                start_coord = str(text[2]).split(',')
                end_coord = str(text[4]).split(',')
                for y in range(int(start_coord[1]), int(end_coord[1]) + 1):
                    for x in range(int(start_coord[0]), int(end_coord[0]) + 1):
                        if lights[1000 * y + x][2] != 0:
                            lights[1000 * y + x][2] += -1

            else:
                print('smth is wrong! (on/off)')
        # toggle
        elif text[0] == 'toggle':
            start_coord = str(text[1]).split(',')
            end_coord = str(text[3]).split(',')
            for y in range(int(start_coord[1]), int(end_coord[1]) + 1):
                for x in range(int(start_coord[0]), int(end_coord[0]) + 1):
                    lights[1000 * y + x][2] += 2

resoult = 0
for element in lights:
    resoult += element[2]

with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(resoult))
print(resoult)