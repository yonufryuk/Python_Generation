# Дополните приведенный код, используя срезы, так чтобы он вывел
# первые 12 символов строки s.
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:12])

# Дополните приведенный код, используя срезы, так чтобы он вывел
# последние 9 символов строки s.
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])

# Дополните приведенный код, используя срезы, так чтобы он вывел
# каждый 7 символ строки s начиная от начала строки.
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])

# Дополните приведенный код, используя срезы, так чтобы он вывел
# строку s в обратном порядке.
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

# На вход программе подается одно слово, записанное в нижнем регистре.
# Напишите программу, которая определяет является ли оно палиндромом.
# Палиндром читается одинаково в обоих направлениях, например слово «потоп».
# p = input()
# s = p[::-1]
# if p == s:
#     print('YES')
# else:
#     print('NO')

# На вход программе подается одна строка. Напишите программу, которая выводит:
# общее количество символов в строке;
# исходную строку повторенную 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символом.
# s = input()
# print(len(s))
# print(s * 3)
# print(s[:1])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# minuslast = len(s) - 1
# print(s[1:minuslast])

# На вход программе подается одна строка. Напишите программу, которая выводит:
# s = input()
# print(s[2:3]) # третий символ этой строки;
# last = len(s)
# slast = last - 1
# sslast = last - 2
# print(s[sslast:slast]) # предпоследний символ этой строки;
# print(s[:5])   # первые пять символов этой строки;
# print(s[:sslast]) # всю строку, кроме последних двух символов;
# print(s[::2]) # все символы с четными индексами;
# print(s[1::2]) # все символы с нечетными индексами;
# print(s[::-1]) # все символы в обратном порядке;
# print(s[::-2]) # все символы строки через один в обратном порядке, начиная с последнего.

# На вход программе подается строка текста. Напишите программу, которая разрежет ее на
# две равные части, переставит их местами и выведет на экран.
# Если длина строки нечетная, то длина первой части должна быть на один символ больше.
# s = input()
# if len(s) == 1:
#     print(s)
# else:
#     midl = len(s) // 2 + len(s) % 2
#     end = len(s)
#     print(s[midl:end], s[:midl], sep='')

