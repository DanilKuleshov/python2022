import hashlib
f = open("input.txt","r")
Key = f.readline()

for i in range(999999):
    newListKey = [Key]
    newListKey.append(i) # В конец списка добавляем наше число (i)
    mystring = ""
    mystring = str(newListKey[0]) + str(newListKey[1]) # Наш ключ + числа в конце
    hash_object = hashlib.md5(mystring.encode()) # Хэшируем наш ключ + числа в конце
    hash_object = hash_object.hexdigest()

    if hash_object[0:5] == "00000": #Проверяем что бы первые 5 чисел были нулями
        res = mystring[len(Key):]
        print(res)
        break
f.close()
with open('output1.txt','w') as output:
    output.write(str(res))