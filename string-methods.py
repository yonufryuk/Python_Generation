# считаем количество символов а
# s = 'aabbAAccDDaa'
# s = s.lower()
# print(s.count('a'))

# проверяем, начинается ли строка с 'www'
# s = 'www.stepik.org'
# print(s.startswith('www'))


# заканчивается ли строка на '.ru'
# s = 'www.stepik.org'
# print(s.endswith('.ru'))

# находим индекс первого вхождения подстроки в исходной строке
# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))

# удаляем все пробелы все пробелы стоящие в начале и конце строки
# s = '     I learn Python language               '
# print(s.strip())

# заменяем все вхождения 'ab' на '123'
# s = 'abcdababa'
# print(s.replace('ab', '123'))

# На вход программе подается строка текста, состоящая из слов, разделенных ровно
# одним пробелом. Напишите программу, которая подсчитывает количество слов в ней.
# s = input()
# print(s.count(' ') + 1)

# На вход программе подается строка генетического кода, состоящая из букв
# А (аденин), Г (гуанин), Ц (цитозин), Т (тимин). Напишите программу,
# которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в
# данную строку генетического кода.
# s = input()
# s = s.lower()
# print('Аденин:', s.count('а'))
# print('Гуанин:', s.count('г'))
# print('Цитозин:', s.count('ц'))
# print('Тимин:', s.count('т'))

# вывести количество строк в которых содержится число 11 минимум 3 раза.
# s = int(input())
# a = 0
# for i in range(s):
#     v = input()
#     if v.count('11') >= 3:
#         a = a + 1
# print(a)

# Программа должна вывести количество цифр в данной строке.
# k = 0
# b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# for c in input():
#     if c in b:
#         k+=1
# print(k)

# Программа должна вывести «YES» если введенная строка заканчивается
# подстрокой .com или .ru и «NO» в противном случае.
# s = input()
# if s.rfind('.com') == len(s)-4 or s.rfind('.ru') == len(s)-3:
#     print('YES')
# else:
#     print('NO')

# вывести символ, который появляется наиболее часто.
# s=input()
# c=0
# a=0
# for i in s:
#     if s.count(i)>=c:
#         c=s.count(i)
#         a=i
# print(a)

# На вход программе подается строка текста. Если в этой строке буква «f» встречается
# только один раз, выведите её индекс. Если она встречается два и более раз,
# выведите индекс её первого и последнего вхождения на одной строке, разделенных
# символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».
# s = input()
# if s.find('f') == -1:
#     print('NO')
# elif s.find('f') == s.rfind('f'):
#     print(s.find('f'))
# else:
#     print(s.find('f'), s.rfind('f'))

# На вход программе подается строка текста, в которой буква «h» встречается
# минимум два раза. Напишите программу, которая удаляет из этой строки первое
# и последнее вхождение буквы «h», а также все символы, находящиеся между ними.
# s = input()
# beg = s.find('h')
# end = s.rfind('h') + 1
# print(s[:beg], s[end:], sep='')