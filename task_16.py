# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
n = int(input("Введите число N: "))
list_1 = list()
for i in range(n):
   # m = int(input())
    m = random.randint(1, 10)
    list_1.append(m)
print(*list_1)
x = int(input("Введите число X: "))
count = 0
for i in range(n):
     if list_1[i] == x:
      count+=1
print("Чиcло ",(x), "встречается в массиве ",(count)," раз(а)")
#print(list_1.count(x))