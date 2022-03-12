# Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# su = 0
# for i in range(len(numbers)):
#     su += numbers[i] ** 2
# print(su)

# подается натуральное число n, а затем n целых чисел. Напишите программу,
# которая для каждого введенного числа xx выводит значение функции
# f(x) = x^2 + 2x + 1
#  каждое на отдельной строке.
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на
# отдельной строке.
# Формат выходных данных
# Программа должна вывести сначала введенные числа, затем пустую строку,
# а затем соответствующие значения функции.
# n = int(input())
# im = []
# su = []
# for _ in range(n):
#     x = int(input())
#     im.append(x)
#     y = x ** 2 + x * 2 + 1
#     su.append(y)
# print(*im, sep='\n')
# print('', sep='\n')
# print(*su, sep='\n')

# подается натуральное число n, а затем n различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение
# из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке,
# не меняя их порядок.
# n = int(input())
# im = []
# for _ in range(n):
#     x = int(input())
#     im.append(x)
# for i in im:
#     if i != min(im) and i != max(im):
#         print(i)

# подается натуральное число nn, а затем nn строк. Напишите программу,
# которая выводит только уникальные строки, в том же порядке, в котором они были введены.
# r = []
# for i in range(int(input())):
#         s = input().lower()
#         if s not in r:
#                 r.append(s)
# print(*r, sep='\n')

# подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается
# поисковый запрос.
# n = int(input())
# im = []
# for _ in range(n):
#     x = input()
#     im.append(x)
# y = input().lower()
# for i in im:
#     if y in i.lower():
#         print(i)


# На вход программе подается натуральное число n, затем nn строк, затем число
# k — количество поисковых запросов, затем kk строк — поисковые запросы. Напишите
# программу, которая выводит все введенные строки, в которых встречаются все
# поисковые запросы.
# n = int(input())
# inpt = [input() for _ in range (n)]
# k = int(input())
# inpt2 = [input() for _ in range (k)]
# for i in range(n):
#     exist = True
#     for j in range(k):
#         if inpt2[j].lower() not in inpt[i].lower():
#             exist = False
#     if exist:
#         print(inpt[i])

# or another variant
# s = [input() for _ in range(int(input()))]
# d = [input() for _ in range(int(input()))]
# for i in s:
#     for j in d:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)

# подается натуральное число n, а затем n целых чисел. Напишите программу,
# которая сначала выводит все отрицательные числа, затем нули, а затем все
# положительные числа, каждое на отдельной строке. Числа должны быть выведены
# в том же порядке, в котором они были введены.
# n = int(input())
# x = [int(input()) for _ in range(n)]
# [print(i) for i in x if i < 0]
# [print(i) for i in x if i == 0]
# [print(i) for i in x if i > 0]