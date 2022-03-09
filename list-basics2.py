# вывел 17-ый элемент списка primes.
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[16]) # нумерация начинается с 0

# используя индексатор, так чтобы он вывел последний элемент списка primes.
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# x = len(primes) - 1
# print(primes[x])

# используя срезы, так чтобы он вывел первые 6 элементов списка primes.
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[:6])

# вывел сумму минимального и максимального элементов списка numbers.
# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# sm = min(numbers) + max(numbers)
# print(sm)

#  вывел среднее арифметическое элементов списка evens.
# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / len(evens)
# print(average)

# элемент списка имеющий значение Green заменился на значение Зеленый,
# а элемент Violet на Фиолетовый
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# for i in range(len(rainbow)):
#     if rainbow[i] == 'Green':
#         rainbow[i] = 'Зеленый'
#     if rainbow[i] == 'Violet':
#         rainbow[i] = 'Фиолетовый'
# print(rainbow)

# вывел элементы списка languages в обратном порядке
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# languages.reverse()
# print(languages)

# используя операторы конкатенации (+) и умножения списка на число (*),
# так чтобы он вывел список:
# [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13].
# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# numbers = numbers1 * 2 + numbers2 * 9 + numbers3
# print(numbers)