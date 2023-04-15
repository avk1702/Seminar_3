# Задача 18: Требуется найти в массиве A[1..N] самый близкий по 
# величине элемент к заданному числу X. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в массиве. В 
# последующих  строках записаны N целых чисел Ai. Последняя строка 
# содержит число X
import random
n = int(input("Введите число N: "))
list_1 = list()
for i in range(n):
   # m = int(input())
    m = random.randint(1, 10)
    list_1.append(m)
print(*list_1)
x = int(input("Введите число X: "))
near = abs(list_1[0] - x)
number = 0
for i in range(1,n):
     count = abs(list_1[i] - x)
     if count < near:
      near = count
      number = i
print("Самый близкий по величине элемент к числу X = ",(list_1[number]))
