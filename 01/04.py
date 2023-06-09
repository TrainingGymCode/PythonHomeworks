# Задача 4:  делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# ------------------------------------------------------------
# x — число журавликов, которое сделали Петя и Серёжа (каждый)
# 2(x + x) = 4x — число журавликов, которое сделала Катя
# x + 4x + x = 6x — общее число журавликов, которое сделали Петя, Катя и Сережа

total = int(input(
    'Введите общее число сделанных журавликов: '))
if (total % 6 == 0):
    x = total // 6
    print(f'{total} -> {x}  {4 * x}  {x}')
else:
    print(
        f'Петя, Катя и Сережа не могли вместе сделать {total} журавликов при таких условиях')
