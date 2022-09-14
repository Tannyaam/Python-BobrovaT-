# Задача 1 (Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции)
# def Find_Sum (list):
#     sum = 0
#     for i in range(1, len(list)):
#         if i % 2 != 0:
#             sum += int(list[i])
#     return sum

# list = input('Задайте список: ').split(' ')
# print(Find_Sum(list))



# Задача 2 (Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д)
# def Pair_Mult (list):
#     if len(list) % 2 != 0:
#         for i in range(0, len(list)//2 + 1):
#             print(f"{list[i]} * {list[len(list) - 1 - i]} = {int(list[i]) * int(list[len(list) - 1 - i])}")
#     else:
#         for i in range(0, len(list)//2):
#             print(f"{list[i]} * {list[len(list) - 1 - i]} = {int(list[i]) * int(list[len(list) - 1 - i])}")

# list = input('Задайте список: ').split(' ')
# Pair_Mult(list)




# Задача 3 (Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов)
# def Find_Dif (list):
#     max = float(list[0]) % 1
#     min = float(list[0]) % 1
#     for i in list[1:]:
#         if float(i) % 1 > max:
#             max = float(i) % 1
#         elif float(i) % 1 < min:
#             min = float(i) % 1
#     return (max - min)

# list = input('Задайте список: ').split(' ')
# print(Find_Dif(list))




# Задача 4 (Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций))
# import string
# def Convert_To_2(num):
#     a = ""
#     while num > 0:
#         a = str(num % 2) + a
#         num = num // 2
#     return a

# num = int(input('Введите число: '))
# print(Convert_To_2(num))




# Задача 5 (Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов)
def Fib(n):
    list_fib_pos = [0, 1]
    list_fib_neg = []
    for i in range(2, n + 1):
        list_fib_pos.append(list_fib_pos[i-2] + list_fib_pos[i-1])
    for i in range(0, n):
        list_fib_neg.append((-1) ** (i + 1) * list_fib_pos[n-i])
    return list_fib_neg + list_fib_pos

num = int(input('Введите число: '))
print(Fib(num))