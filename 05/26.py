# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def num_in_power(num: int, power: int) -> int:
  # power = 0
  if power == 0:
    return 1
  # power > 0
  if (power > 0):
    if power == 1:
      return num
    else:
      return num * num_in_power(num, power - 1)
  # power = 0
  else:
    if power == -1:
      return 1 / num
    else:
      return (1 / num) * num_in_power(num, power - 1)


base = int(input('Input base: '))
power = int(input('Input power: '))

print(f'Number {base} in power {power} is {num_in_power(base, power)}')
