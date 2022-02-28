# num = int(input())
# flag = True
#
# for i in range(2, num // 2 + 1):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# num = int(input())
# flag = True
#
# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# num = int(input())
# flag = True
#
# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         flag = False
#         break
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# Нужно написать программу, которая выводит на экран сумму всех отрицательных
# чисел последовательности и максимальное отрицательное число в
# последовательности. Если отрицательных чисел нет, требуется вывести на
# экран «NO». Программист торопился и написал программу неправильно

# mx = -10**6 - 1
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if 0 > x > mx:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# программу, которая подсчитывает и выводит сумму всех чётных чисел
# последовательности или 0, если чётных чисел в последовательности нет
# s = 0
# for _ in range(7):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# print(s)

# написать программу, которая выводит на экран максимальную цифру числа,
# кратную 33. Если в числе нет цифр, кратных 3,
# требуется на экран вывести «NO».
# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# Нужно написать программу, которая выводит на экран его первую
# (старшую) цифру
# n = int(input())
# while n > 9:  # Ошибка - цикл имеет смысл только в случае если данное натурально число дву- и  более -значное.
#     n //= 10  # Ошибка - нам необходимо постепенно отбрасывать числа до первого, а не выяснять последние из них.
# print(n)

# программу, которая выводит на экран произведение цифр введенного числа
# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)