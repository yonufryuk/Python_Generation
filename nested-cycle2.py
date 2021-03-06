# программу, которая печатает численный треугольник
# с высотой равной n
# p =0
# n = int(input())
# for i in range(n):
#     for j in range(i + 1):
#         print(p+1, end=' ')
#         p+=1
#     print()

# программу, которая печатает численный треугольник
# с высотой равной n
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 2 * i):
#         print(min(j, 2 * i - j), end='')
#     print()

# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит натуральное
# число из отрезка [a;b] с максимальной суммой делителей

# a, b = int(input()), int(input())
# counter = 0 # счетчик подсчета суммы делителей
# number = 1 # число которое будем выводить (минимум 1)
# summa = 0  # тут будет сумма делителей, которую надо будет вывести
# for i in range(a, b + 1):  # проверяем каждое число в [a;b]
#     counter = 0 # обнуляем счетчик для каждого i
#     for j in range(1, i + 1):  # берем по очереди каждый делитель числа от [1 до самого числа]
#         if i % j == 0:  # если число делится на j без остатка, значит j - делитель числа
#             counter += j  # создаем сумму делителей
#     if counter >= summa:  # если сумма делителей больше или равна, чем суммаа делителей предыдущего числа
#         summa = counter  # то counter теперь равно кол-ву делителей этого числа вместо кол-ва предыдущего
#         number = i  # число у которого делителей оказалось больше, теперь равно number
# print(number, summa) # в конце концов, выводим само число (у которого больше делителей) и сумму этих делителей

# На вход программе подается натуральное число nn. Напишите программу,
# выводящую графическое изображение делимости чисел от 1 до n включительно.
# В каждой строке надо напечатать очередное число и столько символов «+»,
# сколько делителей у этого числа
# n = int(input())
# for i in range(1, n + 1):          # циклом перебираем все числа от 1 до n включительно
#     count = 0                      # вводим счетчик, который будет обнуляться каждую новую итерацию
#     for j in range(1, i + 1):      # во внутреннем цикле проверяем каждое из чисел на кол-во делителей
#         if i % j == 0:             # если делитель есть, то ->
#             count += 1             # -> к счетчику добавляем 1, это наши будующие плюсики
#     print(i, '+' * count, sep='')  # вывододим строку с числом и нужным кол-вом плюсов в рамках одной итерации


# На вход программе подается натуральное число nn. Напишите программу,
# которая находит цифровой корень данного числа. Цифровой корень числа n
# получается следующим образом: если сложить все цифры этого числа,
# затем все цифры найденной суммы и повторить этот процесс,
# то в результате будет получено однозначное число (цифра), которое
# и называется цифровым корнем данного числа.
# num = int(input())                # Число на входе, оно же будет и цифровым корнем на выходе.
# while num >= 10:                  # Как только сумма цифр в числе становится меньше 10 выводим результат.
#     sum_last_num = 0              # Накопитель для промежуточных сумм.
#     while num != 0:               # Классический перебор цифр в числе:
#         sum_last_num += num % 10  # считываем последнюю цифру в числе и сумируем,
#         num //= 10                # уменьшаем число на последнюю цифру.
#     num = sum_last_num            # Присваиваем числу значение суммы, внешний цикл проверит, не пора ли
#                                   # на выход. Если нет, то вложенный цикл еще раз просуммирует цифры в числе
# print(num)                        # happy end

# Дано натуральное число nn. Напишите программу, которая выводит
# значение суммы 1!+2!+3!+…+n!.
# from math import factorial  # вызываем функцию для нахождения факториала из модуля math
#
# n = int(input())  # подается натуральное число
# total = 0  # вводится переменная суммы
#
# for i in range(1, n + 1):  # перебираем числа от 1 до n
#     total += factorial(i)  # к сумме добавляем факториал числа i
# print(total)  # выводим сумму факториалов
# или
# n = int(input())
# a = 1
# b = 0
# for i in range(1, n + 1):
#     a *= i
#     b += a
# print(b)

# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит все простые числа от a до b включительно.
"""Простое число делится только на 1 и само на себя. Решаем через счетчик
делителей, или можно модифицировать код из 7.9.3. Для оптимизации кода я
использую тот факт, что все делители кроме самого числа находятся в первой
половине этого числа. И в этом случае у него может быть только один делитель
(равный 1). Также, т.к. 1 не является простым числом, то есть 2 выхода:
1. Просто меняем его на 2, и учитываем это перед внешним циклом (на общий
результат это не повлияет),
2. Или пропускаем этот вариант во внешнем цикле (через continue). Данный
вариант предпочтительнее.
"""

# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     if i == 1:
#         continue                        # Учитываем, что 1 не является простым числом
#     count = 0                           # Задаем счетчик делителей. Тут же он обнуляется перед итерацией
#     for j in range(1, int(i / 2) + 1):  # Все делители числа i находятся в этом диапазоне (кроме него самого)
#         if i % j == 0:                  # Условие делителя
#             count += 1
#     if count == 1:                      # Условие для простого числа с учетом диапазона по j
#         print(i)