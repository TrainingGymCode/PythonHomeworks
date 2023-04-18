# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

count = int(input('Введите кол-во монет: '))

coins = []

for i in range(count):
    coins.append(random.randint(0, 1))

eagle_count = 0
tail_count = 0

for i in range(0, len(coins)):
    if (coins[i] == 1):
        eagle_count += 1
    else:
        tail_count += 1

print(coins)
print(
    f'Нужно перевернуть монет: {min(eagle_count, tail_count)}')
