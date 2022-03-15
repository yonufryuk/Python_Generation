# Напишите функцию draw_box(), которая выводит звездный прямоугольник
# с размерами  14×10 :
# def draw_box():
#     print('*' * 10)
#     for i in range(12):
#         print('*' + ' ' * 8 + '*')
#     print('*' * 10)
#
# draw_box()  # вызов функции

# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный
# треугольник с катетами, равными 10
# def draw_triangle():
#     for i in range(1,11): print('*' * i)
#
# # основная программа
# draw_triangle()  # вызов функции

# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)
# print_number(2, 3, 11)

# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
#
# x = 1
# y = 7
# print(x, y)
# change_us(x, y)
# print(x, y)

# def print_text(text, num):
#     while num > 0:
#         print(text, end='')
#         num -= 1
#
# print_text('Python', 4)


# Звездный треугольник
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
# def draw_triangle(fill, base):
#     for i in range(1, base + 1):
#         print(fill * min(i, base - i + 1))
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)
# one more time
# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 1):
#         print(fill * i)
#     for i in range(base // 2 + 1, 0 , -1):
#         print(fill * i)
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)

# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# def print_fio(name, surname, patronymic):
#     print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())
# name, surname, patronymic = input(), input(), input(),
# print_fio(name, surname, patronymic)
# one more time
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper() + name[0].upper() + patronymic[0].upper())
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)

# Напишите функцию print_digit_sum(), которая принимает одно целое число num и
# выводит на печать сумму его цифр.
# def print_digit_sum(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     print(sum)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)
# one more time
# def print_digit_sum(num):
#     print(sum(int(i) for i in str(num)))
#
# n = int(input())
#
# print_digit_sum(n)