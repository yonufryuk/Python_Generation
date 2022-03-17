# Какой программный код написан с ошибкой?
# def do_something():
#   a = 1
#
# do_something()
# print(a)
#
#   line 6, in <module>
#     print(a)
# NameError: name 'a' is not defined


# Какие из переменных в приведенном ниже коде являются локальными?
#
# def factorial(n):
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
#     return res
#
# number = int(input())
# f = factorial(number)
# answer:
# res
# n
# i


# Python считает переменную локальной для данной функции, если в её коде есть
# хотя бы одна инструкция, модифицирующая значение переменной. В этом случае эта
# переменная считается  локальной и не может быть использована до инициализации.


# Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник
# с основанием и высотой равными 15 и 8 соответственно:
# объявление функции
# def draw_triangle():
#     m = 15
#     for i in range(1, m + 1, 2):
#         print(' ' * ((m - i) // 2) + '*' * i)
#
# # основная программа
# draw_triangle()  # вызов функции
# one more time
# # объявление функции
# def draw_triangle():
#     z = 1
#     for i in range(7, -1, -1):
#         print(' ' * i + '*' * z)
#         z += 2
#
# # основная программа
# draw_triangle()  # вызов функции


# Интернет магазин осуществляет экспресс доставку для своих товаров по цене 1000
# рублей за первый товар и 120 рублей за каждый последующий товар. Напишите
# функцию get_shipping_cost(quantity), которая принимает в качестве аргумента
# натуральное число quantity – количество товаров в заказе и возвращает стоимость доставки.
# # объявление функции
# def get_shipping_cost(quantity):
#     return 1000 + 120 * (quantity - 1)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_shipping_cost(n))


# Биномиальный коэффициент
# from math import factorial
# # объявление функции
# def compute_binom(n, k):
#     return int(factorial(n) / (factorial(k) * factorial(n - k)))
#
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))


# Число словами
# # объявление функции
# def number_to_words(num):
#     s = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто','']
#     if num <= 20:
#         return s[num - 1]
#     else:
#         return s[num // 10 - 1 + 18] + ' ' + s[num % 10 - 1]
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))
# one more time
# # объявление функции
# def number_to_words(num):
#     list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
#     list_2 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
#                'восемнадцать', 'девятнадцать']
#     list_3 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#
#     if 1 <= num <= 10:
#         return list_1[num-1]
#     elif 20 <= num <= 99 and num % 10 == 0:
#         return list_3[num // 10 - 2]
#     elif 20 <= num <= 99:
#         return list_3[num // 10 - 2] + ' ' + list_1[num % 10 - 1]
#     else:
#         return list_2[num % 10 - 1]
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))


# Искомый месяц
# # объявление функции
# def get_month(language, number):
#     monthsRu = { 1 : 'январь', 2 : 'февраль', 3 : 'март', 4 : 'апрель', 5 : 'май', 6 : 'июнь', 7 : 'июль', 8 : 'август', 9 : 'сентябрь', 10 : 'октябрь', 11 : 'ноябрь', 12 : 'декабрь'}
#     monthsEn = { 1 : 'january', 2 : 'february', 3 : 'march', 4 : 'april', 5 : 'may', 6 : 'june', 7 : 'july', 8 : 'august', 9 : 'september', 10 : 'october', 11 : 'november', 12 : 'december'}
#     if language == 'ru':
#         return monthsRu[number]
#     else:
#         return monthsEn[number]
#
# # считываем данные
# lan = input()
# num = int(input())
#
# # вызываем функцию
# print(get_month(lan, num))


# Магическая дата – это дата, когда день, умноженный на месяц, равен числу
# образованному последними двумя цифрами года.
# # объявление функции
# def is_magic(date):
#     day, month, year = date.split('.')
#     return int(day) * int(month) == int(year) % 100
#
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))


# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют
# для презентации шрифтов
# def is_pangram(text):
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     for letter in text.lower():
#         if letter in letters:
#             letters.remove(letter)
#     return len(letters) == 0
#
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))
# one more time
# from string import ascii_lowercase
# # объявление функции
# def is_pangram(text):
#     for i in ascii_lowercase:
#         if i not in text.lower():
#             return False
#     return True
#
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))

