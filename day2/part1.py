with open("input.TXT") as f:
    lines = f.readlines() #СЧИТЫВАЕМ ВСЕ СТРОКИ ДОКУМЕНТА В СПИСКИ
    f.seek(0) #ВОЗВРАЩЕМ КУРСИВ В САМОЕ НАЧАЛО
    res = 0
    for i in range(0, len(lines)): #ОБРАЩАЕМСЯ К КАЖДОЙ СТРОКЕ ЧЕРЕЗ ЦИКЛ "for"

        #ДОСТАЁМ ИЗ КАЖДОЙ СТРОКИ ТОЛЬКО ЧИСЛА
        line = f.readline() #ЧИТАЕМ ПЕРВУЮ СТРОКУ
        lineList = line.replace("\n", "").split("x") #РАЗДЕЛЯЕМ ЭТУ СТРОКУ В СПИСОК ТАК, ЧТО БЫ ОСТАЛИСТЬ ОДНИ ЦИФРЫ ((И УБИРАЕМ /n) replace(<что заменяем>,<на что заменяем>))
        lineList = list(map(int, lineList))
        lineList = sorted(lineList) #УПОРЯДОЧИВАЕТ ЧИСЛА В ПОРЯДКЕ ВОЗРАСТАНИЯ В СПИСКЕ
        res += 2*lineList[0]*lineList[1]+2*lineList[0]*lineList[2]+2*lineList[1]*lineList[2]+lineList[0]*lineList[1]
    print(res)
file = open("output1.TXT", 'w')
d = str(res)
file.write(d)
file.close()