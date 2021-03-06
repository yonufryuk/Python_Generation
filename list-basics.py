# Функция len()
# numbers = [2, 4, 6, 8, 10]
# languages = ['Python', 'C#', 'C++', 'Java']
# print(len(numbers))      # выводим длину списка numbers
# print(len(languages))    # выводим длину списка languages
# print(len(['apple', 'banana', 'cherry']))   # выводим длину списка, состоящего из 3 элементов

# Оператор принадлежности in
# numbers = [2, 4, 6, 8, 10]
# if 2 in numbers:
#     print('Список numbers содержит число 2')
# else:
#     print('Список numbers не содержит число 2')
#
# numbers = [2, 4, 6, 8, 10]
# if 0 not in numbers:
#     print('Список numbers не содержит нулей')

# Индексация
# numbers = [2, 4, 6, 8, 10].
# numbers[0]	2	первый элемент списка
# numbers[1]	4	второй элемент списка
# первый элемент списка numbers[0], а не numbers[1]
# попытка обратиться к элементу списка по несуществующему индексу:
# print(numbers[17])
# вызовет ошибку:
# IndexError: index out of range

# Срезы
# numbers = [2, 4, 6, 8, 10]
# print(numbers[1:3])
# print(numbers[2:5])
# выводит:
# [4, 6]
# [6, 8, 10]

# изменения элементов в заданном диапазоне
# fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
# fruits[2:5] = ['банан', 'вишня', 'киви']
# print(fruits)
# выводит:
# ['apple', 'apricot', 'банан', 'вишня', 'киви', 'lemon', 'mango']

# конкатенации + и умножения на число *
# print([1, 2, 3, 4] + [5, 6, 7, 8])
# print([7, 8] * 3)
# print([0] * 10)
# выводит:
# [1, 2, 3, 4, 5, 6, 7, 8]
# [7, 8, 7, 8, 7, 8]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Следующий программный код:
# a = [1, 2, 3, 4]
# b = [7, 8]
# a += b   # добавляем к списку a список b
# b *= 5   # повторяем список b 5 раз
# print(a)
# print(b)
# выводит:
# [1, 2, 3, 4, 7, 8]
# [7, 8, 7, 8, 7, 8, 7, 8, 7, 8]

# Встроенные функции sum(), min(), max()
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('Сумма всех элементов списка =', sum(numbers))
# выводит:
# Сумма всех элементов списка = 55

# numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
# print('Минимальный элемент =', min(numbers))
# print('Максимальный элемент =', max(numbers))
# выводит:
# Минимальный элемент = -7
# Максимальный элемент = 3333

# Несмотря на всю схожесть списков и строк, есть одно очень важное отличие:
# строки — неизменяемые объекты, а списки – изменяемые.
# s = 'abcdefg'
# s[1] = 'x'    # пытаемся изменить 2 символ (по индексу 1) строки
# приводит к ошибке:
# object does not support item assignment

# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers[1] = 101     # изменяем 2 элемент (по индексу 1) списка
# print(numbers)
# выводит:
# [1, 101, 3, 4, 5, 6, 7]