# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#         break               # останавливаем цикл если встретили делитель числа
# if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# num = int(input())
# number = num
# flag = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     num //= 10
# if flag == True:
#     print('Число', number, 'содержит цифру 7')
# else:
#     print('Число', number, 'не содержит цифру 7')

# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)

# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# программу, которая выводит его наименьший отличный от 1 делитель.
# num = int(input())
# for i in range(2, num + 1):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         print(i)
#         break               # останавливаем цикл если встретили делитель числа

# выводит числа от 11 до nn включительно за исключением:
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.
# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue  # переходим на следующую итерацию
#     print(i)

# n = int(input())
# while n != 0:
#     last = n % 10
#     if last == 7:
#         print('Число', n, 'содержит цифру 7')
#         break
#     n //= 10
# else:
#     print('Число', n, 'не содержит цифру 7')

# n = 0
# while n < 10:
#     n += 2
#     print(n)
# else:
#     print('Цикл завершен.')