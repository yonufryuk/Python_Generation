from random import *
word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз',
             'сделка', 'сочинение', 'покупатель', 'танк', 'затрата', 'строка', 'единица']
# защита от дурака
def is_valid(letter):
    return letter.isalpha() == True
# функция загадывания слова
def get_word():
    word = word_list[randint(1, (len(word_list)))].upper()
    return word
#функция повторной игры
def repeat_game():
    print("Хотите сыграть еще? Напишите да или нет")
    answer = input()
    if answer == "да":
        play()
    else:
        print("Всё пока!")
# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

#функция с основной логикой игры
def play():
    word = get_word()
    word_completion = '*' * len(word)  # строка, содержащая символы * на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте играть в виселицу!')
    print(display_hangman(tries))
    print(word_completion)
    while tries > 0:
        print("Ведите букву или слово")
        text = input().upper()
#обработка ввода слова
        if len(text) > 1 and is_valid(text) and text not in guessed_words:
            guessed_words.append(text)
            if text == word:
                print("Поздравляем, вы угадали слово! Вы победили!")
                repeat_game()
            elif text != word and tries == 1:
                print("Неверное слово. Вы проиграли(((")
                print("Загаданное слово - ", word)
                tries -=1
                print(display_hangman(tries))
                repeat_game()
                break
            else:
                print("Неверное слово. Попробуйте еще раз")
                tries -= 1
                print(display_hangman(tries))
        elif len(text) > 1 and is_valid(text) and text in guessed_words:
            print("Такое слово уже пробовали. Попытка не защитана")
#обработка ввода буквы
        elif len(text) == 1 and is_valid(text) and text not in guessed_letters:
            guessed_letters.append(text)
            if text in word:
                for i in range(len(word)):
                    if word[i] == text:
                        word_completion = word_completion[:i] + text + word_completion[i+1:]
                print(word_completion)
                print("Вы угадали букву", text)
                if word_completion == word:
                    print("Поздравляем, вы угадали слово! Вы победили!")
                    repeat_game()
            elif text not in word and tries == 1:
                print("Неверная буква. Вы проиграли(((")
                print("Загаданное слово - ", word)
                tries -= 1
                print(display_hangman(tries))
                repeat_game()
                break
            elif text not in word:
                print("Неверная буква. Попробуйте еще раз")
                tries -= 1
                print(display_hangman(tries))
        elif len(text) == 1 and is_valid(text) and text in guessed_letters:
            print("Такую букву уже пробовали. Попытка не защитана")
        else:
            print("Вводите только буквы или слова")
play()