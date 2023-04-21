# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input('Введите число N (длина списка): '))

arr = []

for i in range(n):
  arr.append(random.randint(1, 10))

print(*arr)

x = int(input('Введите число X: '))

closest = arr[0]

for i in range(1, len(arr)):
  if abs(arr[i] - x) < abs(closest - x):
    closest = arr[i]

print(closest)
