# Дополните приведенный код, используя списочное выражение так, чтобы получить
# новый список, содержащий строки исходного списка с удаленным первым символом.
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [s[1:] for s in keywords]
# print(new_keywords)

# Дополните приведенный код, используя списочное выражение, так чтобы получить новый список,
# содержащий длины строк исходного списка.
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(i) for i in keywords]
# print(lengths)

# Дополните приведенный код списочным выражением, чтобы получить новый список,
# содержащий только слова длиной не менее пяти символов (включительно).
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [s for s in keywords if len(s) > 4]
# print(new_keywords)

# Дополните приведенный код, используя списочное выражение,
# так чтобы получить список всех чисел палиндромов от 100100 до 10001000.
# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
# print(palindromes)

# На вход программе подается натуральное число nn. Напишите программу, использующую списочное выражение,
# которая создает список содержащий квадраты чисел от 11 до nn, а затем выводит его элементы построчно,
# то есть каждый на отдельной строке.
# spisok=[i**2 for i in range(1,int(input())+1)]
# print(*spisok, sep='\n')

# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, использующую списочное выражение, которая выведет
# кубы указанных чисел также на одной строке.
# print(*[int(i) ** 3 for i in input().split()])
#
# n = [int(i)**3 for i in input().split()]
# for _ in n:
#     print(_, end=" ")

# На вход программе подается строка текста, содержащая слова.
# Напишите программу, которая выводит слова введенной строки в столбик.
# print (*input().split(),sep='\n')
#
# lst = [s for s in input().split()]
# print(*lst, sep='\n')

# На вход программе подается строка текста. Напишите программу,
# использующую списочное выражение, которая выводит все цифровые символы данной строки.
# lst = [i for i in input() if i.isdigit()]
# print(*lst, sep='')
#
# print(*[i for i in input() if i in "0123456789"], sep='')


# На вход программе подается строка текста, содержащая целые числа. Напишите программу,
# использующую списочное выражение, которая выведет квадраты четных чисел, которые не
# оканчиваются на цифру 4.
# digit = [int(i)**2 for i in input().split()
#          if (int(i)**2) % 10 != 4 and (int(i)**2) % 2 == 0]
#
# print(*digit, sep=' ')
#
# print(*[int(i) ** 2 for i in input().split() if i[-1] in "046"])

