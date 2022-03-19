# программа генерирует случайное число в диапазоне от 1 до 100 и просит
# пользователя угадать это число. Если догадка пользователя больше случайного числа,
# то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа, то программа должна вывести сообщение
# 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число,
# то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'

# import random
# print('Угадай число от 1 до 100')
# num_ran = random.randint(1, 100)
# while True:
#     num_in = int(input('Введите свой вариант: '))
#     if num_in > num_ran:
#         print('Слишком много, попробуйте еще раз')
#         continue
#     elif num_in < num_ran:
#         print('Слишком мало, попробуйте еще раз')
#         continue
#     else:
#         print('Вы угадали, поздравляем!')
#         print('Может хотите еще раз сыграть?', 'Введите "Да" или "Нет"')
#         num_in_in = input()
#         if num_in_in == 'Да':
#             num_ran = random.randint(1, 100)
#             continue
#         elif num_in_in == 'Нет':
#             print('Спасибо за игру!')
#             break



# Тимур загадал число от 1 до n. За какое наименьшее количество вопросов (на которые
# Тимур отвечает "больше" или "меньше") Руслан может гарантированно угадать число Тимура?
# n=int(input())
# k=0
# a=n
# while n>=1:
#     k=k+1
#     n=n//2
# if a==2**(k-1):
#     print(k-1)
# else:
#     print(k)

# one more time
# n=int(input())
# count = 0
# while n > 1:
#     n = n/2
#     count+=1
# print(count)

# one more time
# from math import log, ceil
# print(ceil(log(int(input()), 2)))

# one more time
# from math import log2, ceil
# n = int(input())
# print(ceil(log2(n)))


# угадайка
# import random
#
# def is_valid(player_num):
#     return player_num.isdigit() and 1 <= int(player_num) <= n
#
# print('Добро пожаловать в числовую угадайку')
# n = int(input('Правая граница: '))
# num = random.randint(1, n)
# # print(num)
# count = 1
# player_num = input(f'Число от 1 до {n}: ')
# while True:
#     count += 1
#     while is_valid(player_num) == False:
#         print('А может быть все-таки введем целое число от 1 до 100?')
#         player_num = input()
#         is_valid(player_num)
#     if int(player_num) < num:
#         print('Ваше число меньше загаданного, попробуйте еще разок')
#         player_num = input()
#         continue
#     elif int(player_num) > num:
#         print('Ваше число больше загаданного, попробуйте еще разок')
#         player_num = input()
#         continue
#     elif int(player_num) == num:
#         print(count)
#         print('Вы угадали, поздравляем!')
#         print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
#         print('Новая игра? (Да / Нет)')
#         m = input()
#         if m == 'Да':
#             num = random.randint(1, 100)
#             print(num)
#             player_num = input('Число от 1 до 100: ')
#             count = 0
#             continue
#         else:
#             break

# без повтора
# from random import *
# random_number = randint(1, 100)
# def is_valid(num):
#     return num.isdigit() and 1 <= int(num) <= 100
# print('Добро пожаловать в числовую угадайку')
# while True:
#     answer = input("Введите число: ")
#     if is_valid(answer) == True:
#         num = int(answer)
#         if num > random_number:
#             print("Ваше число больше загаданного, попробуйте еще разок")
#         if num < random_number:
#             print("Ваше число меньше загаданного, попробуйте еще разок")
#         if num == random_number:
#             print("Вы угадали, поздравляем!")
#             print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
#             break
#     else:
#         print("А может быть все-таки введем целое число от 1 до 100?")



# еще разок
# # 1. Заголовок программы:
#
# import random                    # подключаем модуль
#
# number = random.randint(1, 101)  # генерируем случайное число от 1 до 100
#
# print('Добро пожаловать в числовую угадайку')
# # 2.  Функция проверки введенных данных на корректность:
#
# def is_valid(num):
#     if num.isdigit():
#         num = int(num)
#         if 1 <= num <= 100:
#             return True
#         else:
#             return False
#     else:
#         return False
# # 3. Основной цикл программы:
#
# import random                    # подключаем модуль
#
# number = random.randint(1, 101)  # генерируем случайное число от 1 до 100
#
# print('Добро пожаловать в числовую угадайку')
#
# while True:
#     response = input('Введите число от 1 до 100:')
#     if not is_valid(responce):
#         print('А может быть все-таки введем целое число от 1 до 100?')
#         continue
#     response = int(response)
# # 4. Сравнение введенного числа с загаданным числом:
#
# import random                    # подключаем модуль
#
# number = random.randint(1, 101)  # генерируем случайное число от 1 до 100
#
# print('Добро пожаловать в числовую угадайку')
#
# while True:
#     response = input('Введите число от 1 до 100:')
#     if not is_valid(responce):
#         print('А может быть все-таки введем целое число от 1 до 100?')
#         continue
#     response = int(response)
#
#     if val < number:
#         print('Ваше число меньше загаданного, попробуйте еще разок')
#     elif val > number:
#         print('Ваше число больше загаданного, попробуйте еще разок')
#     else:
#         print('Вы угадали, поздравляем!')
#         break
#
# print('Спасибо, что играли в числовую угадайку. Еще увидимся...')