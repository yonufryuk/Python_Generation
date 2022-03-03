# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# for i in range(8):
#     for j in range(6):
#         print('*', end='')
#     print()

# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# программу, которая печатает таблицу размером n×3 состоящую из данного
# числа (числа отделены одним пробелом).
# n = int(input())
# for i in range(n):
#     print(n, n, n)

# Напишите программу, которая печатает таблицу размером n * 5,
# где в i - ой строке указано число i(числа отделены одним
# пробелом).
# n = int(input())
# for i in range(n):
#     m = i + 1
#     print(m, m, m, m, m)

# Дано натуральное число n (n ≤ 9). Напишите программу,
# которая печатает таблицу сложения для всех чисел от 1 до n в соответствии
# с примером.

# n = int(input())
# for i in range(1, n + 1):
#     for  j in range(1, 10):
#         print(i,'+', j, '=', i + j)
#     print()

# звездный треугольник с основанием, равным n
# m = int(input())
# n = m // 2 + 1
# for i in range(1, n + 1):
#     print(i * '*')
# for j in range(n - 1, 0, -1):
#     print(j * '*')

# печатает численный треугольник
# n = int(input())
# for i in range(1, n + 1):
#     print(i * str(i))

# являющихся решением уравнения 12x+13y = 777
# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)

# решением уравнения x^2+y^2+z^2 = 2020
# total = 0
# for x in range(1, 45):
#     for y in range(1, 45):
#         for z in range(1, 45):
#             if x ** 2 + y ** 2 + z ** 2 == 2020:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

# Решите уравнение в натуральных числах 28n + 30 k + 31 m = 365.
# total = 0
# for x in range(1, 13):
#     for y in range(1, 13):
#         for z in range(1, 13):
#             if x * 28 + y * 30 + z * 31 == 365:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

# Решите уравнение в натуральных числах 10n + 5 k + 0.5 m = 100.
# total = 0
# for x in range(1, 11):
#     for y in range(1, 21):
#         for z in range(1, 101):
#             if x * 10 + y * 5 + z * 0.5 == 100 and x + y + z == 100:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

# Гипотеза Эйлера о сумме степеней
# p = [x ** 5 for x in range(151)]
# pw = set(p)
# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 s = p[a] + p[b] + p[c] + p[d]
#                 if s in pw:
#                     print(a, b, c, d, p.index(s))
#                     print(a + b + c + d + p.index(s))