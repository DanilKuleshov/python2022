file = open("input.txt", 'r')
List = file.readline()
op = 0
cl = 0
tt = 0

for i in range(0, len(List)):
    tt +=1
    if List[i] == '(':
        op += 1
    if List[i] == ')':
        cl += 1
    if op - cl == -1:
        break
resoult = op - cl
print("Санта впервые впервые на " + str(resoult) + " этаже на " + str(tt) + " позиции.")
file.close()
f = open("output2.txt", 'w')
g = str(resoult)
f.write(g)
f.close()
