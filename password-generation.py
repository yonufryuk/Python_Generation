import random

chars = ""
questions = {"Будут ли включать в себя пароли цифры?(да / нет)": "0123456789",
          "Будут ли включать в себя пароли ПРОПИСНЫЕ буквы? (да / нет)": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
          "Будут ли включать в себя пароли символы? (да / нет)": "!#$%&*+-=?@^_",
          "Будут ли включать в себя пароли строчные буквы? (да / нет)": "abcdefghijklmnopqrstuvwxyz"}

# Функция проверки правильности ввода значения ДА или НЕТ
def correct_input_text(txt):
   while True:
      if txt != "да" and txt != "нет":
         txt = input("Введите корректный ответ: (да / нет)\n").lower().strip()
         continue
      break
   return txt

# Функция проверки правильности ввода цифрового значения
def correct_input_digit(num):
   while True:
      if not num.isdigit():
         num = input("Введите целое число!\n")
         continue
      break
   return num

# Функция генерации пароля из строки
def password_gen(symbols):
   return random.choice(symbols)

# Входные данные, проверка
how_many_passwords = input("Сколько паролей необходимо создать?\n")
how_many_passwords = correct_input_digit(how_many_passwords)

password_len = input("Какой длины должен быть пароль?\n")
password_len = correct_input_digit(password_len)

# цикл создания строки с символами
for key in questions:
   print(key)
   text = input()
   text = correct_input_text(text)
   if text == "да":
      chars += questions[key]

if len(chars) == 0:
   print("Вы не ввели значения для генерации паролей. Попробуйте еще раз")
   quit()

# исключение неоднозначных символов
is_not_typical_chars = input("Будут ли исключены неоднозначные символы (il1Lo0O)? (Да / Нет)\n").lower()
is_not_typical_chars = correct_input_text(is_not_typical_chars)
if is_not_typical_chars == "да":
   for c in 'il1Lo0O':
      chars = chars.replace(c, "")

# цикл генерации паролей
print("Ваши пароли:")
for _ in range(int(how_many_passwords)):
   password = ""
   for _ in range(int(password_len)):
      password += password_gen(chars)
   print(password)
