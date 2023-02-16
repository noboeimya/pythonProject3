# Задача 26
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# Пример:
# A = 3; B = 5 -> 243 (3**5)
# A = 2; B = 3 -> 8

# Пример решения задачи без рекурсии

# a = int(input('вводим число N: '))
# b = int(input('вводим степень М: '))
# n = a ** b
# print('результат введения N^M = ', n)

# пример решения задачи с рекурсией
def exponent(n,d):
    if (d == 1):
        return (n)
    if (d != 1):
        return(n * exponent(n,d - 1))
n = int(input('введите число: '))
d = int(input('введите его степень: '))
print('возведение в степень ровно: ', exponent(n,d))


