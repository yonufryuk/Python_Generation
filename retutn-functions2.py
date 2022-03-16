# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает
# в качестве аргументов три натуральных числа, и возвращает значение True если
# существует невырожденный треугольник со сторонами side1, side2, side3 и False
# в противном случае.
# # объявление функции
# def is_valid_triangle(a, b, c):
#     if (a < b + c) and (b < a + c) and (c < a + b):
#         return True
#     else:
#         return False
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))


# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное
# число и возвращает значение True если число является простым и False в противном случае.
# # объявление функции
# def is_prime(a):
#     if a == 1:
#         return False
#     for i in range(2, a // 2 + 1):
#         if (a % i == 0):
#             return False
#     return True
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))


# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное
# число num и возвращает первое простое число большее числа num.
# # объявление функции
# def get_next_prime(num):
#     num += 1
#     for i in range(2, num):
#         if num % i == 0:
#             return get_next_prime(num)
#     return num
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))


# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 88 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.
# # объявление функции
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     for c in password:
#         if c.isupper():
#             flag1 = True
#         elif c.islower():
#             flag2 = True
#         elif c.isdigit():
#             flag3 = True
#     return flag1 and flag2 and flag3
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))
#
# one more time
# # объявление функции
# def is_password_good(password):
#     upp = [i for i in password if i.isupper()]
#     low = [i for i in password if i.islower()]
#     dig = [i for i in password if i.isdigit()]
#     return all([len(password) >= 8, upp, low, dig])
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))


# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов
# два слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину
# и отличаются ровно в 1 символе и False в противном случае.
# # объявление функции
# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     count = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#     if count == 1:
#         return True
#     else:
#         return False
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))


# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и
# возвращает значение True если указанный текст является палиндромом и False в противном случае.
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми,
# а также игнорируйте пробелы, а также символы , . ! ? -.
# # объявление функции
# def is_palindrome(text):
#     textt = [i.lower() for i in text if i not in (',.!?- ')]
#     return textt == textt[::-1]
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))



# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с
# необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента
# строковое значение пароля password и возвращает значение True если пароль является
# действительным паролем BEEGEEK банка и False в противном случае.
# # объявление функции
# def isPrime(n):
#     if n % 2 == 0: return(n == 2)
#     d = 3
#     while d * d <= n and n % d != 0: d += 2
#     return(d * d > n)
#
# def isPalindrom(n):
#     n = str(n)
#     return(n == n[::-1])
#
# def isEven(n): return(not n % 2)
#
# def is_valid_password(password):
#     try:
#         a, b, c = map(int, password.split(':'))
#         return(isPalindrom(a) and isPrime(b) and isEven(c))
#     except: return(False)
#
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))


# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую
# строку text, состоящую из символов ( и ) и возвращает значение True если поступившая на
# вход строка является правильной скобочной последовательностью и False в противном случае.
# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только
# из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.
# # объявление функции
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return not text
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))


# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента
# строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
# # объявление функции
# def convert_to_python_case(text):
#     s = ''
#     for el in text:
#         if el.isupper():
#             s += '_'
#         s += el.lower()
#     return s[1:]
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))
