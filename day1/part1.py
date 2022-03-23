file = open("input.txt", 'r')
List = file.readline()
op = 0
cl = 0

for i in range(0, len(List)):
    if List[i] == '(':
        op += 1
    if List[i] == ')':
        cl += 1
resoult = op - cl
print("Количество раз когда Санта поднимется на этаж: " + str(op))
print("Количество раз когда Санта опустится на этаж: " + str(cl))
print("Санта окажется на " + str(resoult) + " этаже.")
file.close()
f = open("output1.TXT", 'w')
g = str(resoult)
f.write(g)
f.close()
