# 1. Заголовок программы:
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
sym_exapt = 'il1Lo0O'

chars =''

# 2.  Считывание пользовательских данных:
quantity = int(input('Какое количество паролей необходимо сгенерировать?: '))
width = int(input('А теперь длина паролей: '))

numbers = input('Включать ли цифры (0 - 9)? [Y/Д]: ').upper()
lower_letter = input('Включать ли прописные буквы (a - z)? [Y/Д]: ').upper()
upper_letters = input('Включать ли строчные буквы (A - Z)? [Y/Д]: ').upper()
symbols = input('Включать ли символы (!#$%&*+-=?@^_)? [Y/Д]: ').upper()
exapt_s = input('Исключать ли неоднозначные символы (il1Lo0O)? [Y/Д]: ').upper()

# 3. Настройка генерируемых паролей:
if numbers in ['Y', 'Д']:
    chars += digits
if lower_letter in ['Y', 'Д']:
    chars += lowercase_letters
if upper_letters in ['Y', 'Д']:
    chars += uppercase_letters
if symbols in ['Y', 'Д']:
    chars += punctuation
if exapt_s in ['Y', 'Д']:
    for i in sym_exapt:
        chars = chars.replace('i', '')

# 4. Функция генерации пароля:
def generate_password(width, char):
    while width > 0:
        password = random.sample(chars, width)
        width -= 1
        return password

# 5. Генерация нужного количества паролей:
print()
for i in range(quantity):
    print(*generate_password(width, chars), sep='')