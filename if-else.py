# word = input()
# if word == 'Python':
#     print('ДА')
# else:
#     print('НЕТ')

# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)

# i = int(input())
# if i % 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')

# a = input()
# b = input()
# if a == b:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# num = int(input())
# a = num % 10
# b = (num // 10) % 10
# c = (num // 100) % 10
# d = num // 1000
# if a + d == c - b:
#     print('ДА')
# else:
#     print('НЕТ')

# a = int(input())
# if a > 17:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# a = int(input())
# a1 = int(input())
# a2 = int(input())
# if a2 - a1 == a1 - a:
#     print('YES')
# else:
#     print('NO')

# a1 = int(input())
# a2 = int(input())
# if a2 > a1:
#     print(a1)
# else:
#     print(a2)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a > b:
#     a = b
# if c > d:
#     c = d
# if a > c:
#     a = c
# print(a)

# a = int(input())
# if a < 14:
#     print('детство')
# if a > 13 and a < 25:
#     print('молодость')
# if a > 24 and a < 60:
#     print('зрелость')
# if a >59:
#     print('старость')

# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
# if a1 > 0:
#     a2 = a1
# else:
#     a2 = 0
# if b1 > 0:
#     b2 = b1
# else:
#     b2 = 0
# if c1 > 0:
#     c2 = c1
# else:
#     c2 = 0
# print(a2 + b2 + c2)

# age = int(input('Сколько вам лет?: '))
# grade = int(input('В каком классе вы учитесь?: '))
# city = input('В каком городе вы живете?: ')
# if age >= 12 and grade >= 7 and city == 'Москва':
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')

# age = int(input('Сколько вам лет?: '))
# grade = int(input('В каком классе вы учитесь?: '))
# city = input('В каком городе вы живете?: ')
# if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')

# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')

# a = 7
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)

# num = int(input())
# d3 = num % 10
# d2 = num % 100 // 10
# d1 = num // 100
# if d3 != d2 and d3 != d1 and d2 != d1:
#     print('Цифры различны')
# else:
#     print('Цифры не различны')

# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')

# x = int(input())
# if (-30 < x < -1) or (7 < x < 26):
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# x = int(input())
# if (x % 7 == 0 or x % 17 == 0) and 999 < x < 10000:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# if (a < b + c) and (b < a + c) and (c < a + b):
#     print('YES')
# else:
#     print('NO')

# x = int(input())
# if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a == c or b == d:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (c == a or c == a - 1 or c == a + 1) and (d == b or d == b - 1 or d == b + 1):
#     print('YES')
# else:
#     print('NO')
