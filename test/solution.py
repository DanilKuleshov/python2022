# 24 Троллейбусы 

# Откроем наш input файл 
f = open("input.txt")

# Зададим переменные
N = 0 # количество человек
k = 0 # время через которое приходит троллейбус
str1 = '' # первая строка файла input
str2 = '' # вторая строка файла input (времена всех пассажиров, во сколько они пришли на остановку)
cup = 0 # переменная для работы в дальнейшей сортировке

case = 0 # суммарное время ожидания троллейбуса для всех пассажиров
List = [] # список в который будет занесён str2
List2 = []
List3 = []

str1 = f.readline() # считываем первую строку 
str2 = f.readline() # считываем вторую строку 

# С помощью метода split присвоим значения константам N и k
k = int(str1.split()[0])
N = int(str1.split()[1]) 

[List.append(int(i)) for i in str2.split()] # заносим в список значения str2 


# Старым, добрым, но к сожалению неоптимизированным методом пузырька отсортируем список List в порядке возрастания
for i in range(len(List)-1):        
	for b in range(len(List)-1):
		if List[b] > List[b+1]:
			cup = List[b]
			List[b] = List[b+1]
			List[b+1] = cup

# Находим значение по первому параметру взяв все возможные варианты времени приезда трллейбуса
g = 0

for i in range(k):
	case = 0
	g = i
	p = -1
	logic = True
	while logic:         
		if g - List[p+1] >= 0:
			case = case + (g - List[p+1])
			p += 1
			if p == N-1:
				logic = False
		else: 
			g += k
	List2.append(case) 


# Находим индекс нужного значения в списке по первому условию
res1 = List2.index(min(List2))

x = res1
logic = True
p = -1
while logic:
	if (x - List[p+1]) >= 0:
		List3.append(x - List[p+1])
		p += 1
		if p == N-1:
			logic = False
	else:
		x += k

index_maxraz = List3.index(max(List3))

GG = List[index_maxraz]
while GG > k:
	GG = GG - k



f.close()
o = open('output.txt', 'w')
o.write(str(res1))
o.write('\n')
o.write(str(GG))
o.close()


