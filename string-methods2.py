# состоит ли исходная строка из буквенно-цифровых символов
# состоит ли исходная строка из буквенных символов
# состоит ли исходная строка только из цифровых символов
# s = 'aabbAA111ccDDaa'
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())

# являются ли все буквенные символы исходной строки строчными (имеют нижний регистр)
# s = 'aabb!@#$11cc'
# print(s.islower())

# являются ли все буквенные символы исходной строки заглавными (имеют верхний регистр)
# s = 'AAb!@#$11CC'
# print(s.isupper())

# состоит ли исходная строка только из пробельных символов
# s = '    abbc    '
# print(s.isspace())

# используя форматирование строк с помощью метода format, так чтобы он вывел текст:
#
# «In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).
# year = 2010
# price = '10k'
# money = 'Bitcoin'
# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, money)
# print(s)
# или
# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
# print('In {}, someone paid {} {} for two pizzas.'.format(year, amount, currency))