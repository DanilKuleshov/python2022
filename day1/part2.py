with open('input.txt', 'r') as INPUT:
    List = INPUT.readline()
    op = 0
    cl = 0
    cnt = 0

    for i in range(0, len(List)):
        cnt+=1
        if List[i] == '(':
            op += 1
        if List[i] == ')':
            cl += 1
        if op - cl == -1:
            break

with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(cnt))
