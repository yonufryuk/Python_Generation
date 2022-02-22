# x = int(input())
# y = int(input())
# if x > 0:
#     if y > 0:
#         print('Первая четверть')
#     else:
#         print('Четвертая четверть')
# else:
#     if y > 0:
#         print('Вторая четверть')
#     else:
#         print('Третья четверть')

# if grade >= 90:
#     print(5)
# else:
#     if grade >= 80:
#         print(4)
#     else:
#         if grade >= 70:
#             print(3)
#         else:
#             if grade >= 60:
#                 print(2)
#             else:
#                 print(1)

# grade = int(input('Введите вашу отметку: '))
#
# if grade >= 90:
#     print(5)
# elif grade >= 80:
#     print(4)
# elif grade >= 70:
#     print(3)
# elif grade >= 60:
#     print(2)
# else:
#     print(1)

# a, b, c = int(input()), int(input()), int(input())
# if a == b:
#     if b == c:
#         print(3)
#     else:
#         print(2)
# else:
#     if a == c:
#         print(2)
#     else:
#         if b == c:
#             print(2)
#         else:
#             print(0)

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print(3)
# elif a == b != c:
#     print(2)
# elif a != b == c:
#     print(2)
# elif a == c != b:
#     print(2)
# else:
#     print(0)

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print(3)
# elif a == b != c or a != b == c or a == c != b:
#     print(2)
# else:
#     print(0)

# a, b = int(input()), int(input())
# if a > b:
#     print('NO')
# elif b > a:
#     print('YES')
# else:
#     print('Don\'t know')

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a == b or b == c or a == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# a, b, c = int(input()), int(input()), int(input())
# if a < b < c or a > b > c:
#     print(b)
# elif b < c < a or b > c > a:
#     print(c)
# else:
#     print(a)

# m = int(input())
# if m == 2:
#     print('28')
# elif m <= 7:
#     print(30 + m%2 )
# else:
#     print(31 - m%2 )

# n = int(input())
# if n < 60:
#     print('Легкий вес')
# elif n < 64:
#     print('Первый полусредний вес')
# elif n < 69:
#     print('Полусредний вес')

# a, b = int(input()), int(input())
# s = input()
# if s == '+':
#     print(a + b)
# elif s == '-':
#     print(a - b)
# elif s == '*':
#     print(a * b)
# elif s == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(a / b)
# else:
#     print('Неверная операция')

# color1, color2 = input(), input()
# if color1 == 'красный' and color2 == 'синий' or (color1 == 'синий' and color2 == 'красный'):
#     print('фиолетовый')
# elif color1 == 'желтый' and color2 == 'синий' or (color1 == 'синий' and color2 == 'желтый'):
#     print('зеленый')
# elif color1 == 'красный' and color2 == 'желтый' or (color1 == 'желтый' and color2 == 'красный'):
#     print('оранжевый')
# elif color1 == 'красный' and color2 == 'красный' or color1 == 'желтый' and color2 == 'желтый' or color1 == 'синий' and color2 == 'синий':
#     print(color1)
# else:
#     print('ошибка цвета')

# n = int(input())
#
# if n < 0 or n > 36:
#     print('ошибка ввода')
# elif n == 0:
#     print('зеленый')
# elif 1 <= n <= 10:
#     if n % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 11 <= n <= 18:
#     if n % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# elif 19 <= n <= 28:
#     if n % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 29 <= n <= 36:
#     if n % 2 == 0:
#         print('красный')
#     else:
#         print('черный')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a2 < a1:
#     if b2 < a1:
#         print('пустое множество')
#     elif b2 == a1:
#         print(b2)
#     elif a1 < b2 <= b1:
#         print(a1, b2)
#     elif b2 > b1:
#         print(a1, b1)
# elif a2 == a1:
#     if b2 <= b1:
#         print(a2, b2)
#     else:
#         print(a2, b1)
# elif a2 < b1:
#     if b2 <= b1:
#         print(a2, b2)
#     else:
#         print(a2, b1)
# elif a2 == b1:
#     print(a2)
# else:
#     print('пустое множество')
