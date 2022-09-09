# Задача 1 (Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр)
n = float(input('Введите число N: '))
str_n = str(n)
sum = 0

for i in range(len(str_n)):
    if str_n[i] == ',' or str_n[i] == '.':
        j = len(str_n) - i - 1

n_num = n * (10**j)

for i in range(len(str_n) - 1):
    sum = sum + n_num % 10
    n_num = n_num // 10
print(sum)

# Задача 2 (Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N)
# n = int(input('Введите число N: '))
# arr = [1]
# for i in range(1,n):
#     arr.append(arr[i-1] * (i + 1))

# print(f"{arr}")


# Задача 3 (Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму)
# k = int(input('Введите число k: '))
# sum = 0

# for i in range(1,k+1):
#     sum = sum + (1 + 1/i)**i

# print(sum)


# Задача 4 (Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных пользователем через пробел позициях)

# from random import randint


# n = int(input('Введите число N: '))
# arr = []
# for i in range(n):
#     arr.append(randint(-n, n))

# pos = input('Введите позиции элементов ')
# mult = 1
# for i in range(len(pos)):
#     if pos[i] != ' ':
#         j = int(pos[i])
#         mult = mult * arr[j]

# print(f"{arr}")
# print(mult)


# Задача 5 (Реализуйте алгоритм перемешивания списка)
# import random
# n = ['a', 'b', 'c', 'd', 'e', 'f']
# random.shuffle(n)
# print(n)