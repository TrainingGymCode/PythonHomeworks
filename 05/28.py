# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

arg1 = int(input('Input argument 1: '))
arg2 = int(input('Input argument 2: '))

def sum_of_two_args(arg1, arg2):
  if arg2 == 0:
    return arg1
  else:
    decr = 1 if arg2 > 0 else -1
    return decr + sum_of_two_args(arg1, arg2 - decr)

print(f'Summ of {arg1} and {arg2} is {sum_of_two_args(arg1, arg2)}')
