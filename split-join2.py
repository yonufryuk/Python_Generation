# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

#  подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.
# s = input()
# words = s.split()
# for i in range(len(words)):
#     print(words[i], sep='\n')
# variant nomer2
# print(*input().split(), sep='\n')

# программе подается строка текста, содержащая имя, отчество и фамилию человека.
# Напишите программу, которая выводит инициалы человека.
# s = input()
# l = s.split()
# for i in range(len(l)):
#     a = l[i]
#     print(a[0], end='.')
# variant nomer2
# print('.'.join([name[0] for name in input().split()]), end='.')

# программе подается одна строка с корректным именем файла в операционной системе Windows.
# Напишите программу, которая разбирает строку на части, разделенные символом "\".
# Каждую часть вывести в отдельной строке.
# s = input()
# folder = s.split('\\')
# print(*folder, sep='\n')
# variant nomer2
# print(*input().split(chr(92)), sep='\n')

# подается строка текста, содержащая целые числа. Напишите программу, которая по заданным
# числам строит столбчатую диаграмму.
# numbers = input().split()
# for i in range(len(numbers)):
#     print('+' * int(numbers[i]))
# variant nomer2
# for i in input().split():
#     print('+' * int(i))

# подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу,
# которая определяет является ли введенная строка текста корректным ip-адресом.
# s = input().split('.')
# for i in s:
#     if int(i) < 0 or int(i) > 255:
#         print('НЕТ')
#         break
# else:
#     print('ДА')

#  подается строка текста и строка разделитель. Напишите программу, которая вставляет указанный
#  разделитель между каждым символом введенной строки текста.
# print(*list(input()), sep=input())
# variant nomer2
# s = input()
# spacer = input()
# print(spacer.join(s))

# подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел.
# Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг
# другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо
# посчитать.
# numbers = input().split()
# count = 0
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             count += 1
# print(count)
