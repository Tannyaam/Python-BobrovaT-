# Задача 1 (Вычислить число c заданной точностью d)
from operator import index
from random import randint, random


def Given_Accuracy(num, accuracy):
    index = 0
    for i in range(len(accuracy)):
        print('len=', len(accuracy))
        if (accuracy[i] == '.') or (accuracy[i] == ','):
            index = i
            print(index)
            break
    return round(num, len(accuracy) - index - 1)

# import math
# num = math.pi
# accuracy = str(input('Введите число, которое определяет точность: '))
# print(Given_Accuracy(num, accuracy))

# Задача 2 (Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N)
def Find_Multipliers(num):
    multipliers = []
    for i in range(2, num + 1):
        while num % i == 0:
            multipliers.append(i)
            num //= i
    return multipliers

# num = int(input('Введите число '))
# print(Find_Multipliers(num))


# Задача 3 (Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности)
def Unique_Elements(list):
    list_of_unique_el = []
    for i in list:
        count = 0
        for j in list:
            if (i == j):
                count += 1
        if count == 1:
            list_of_unique_el.append(i)
    return list_of_unique_el

# list = input('Введите последовательность чисел: ').split(' ')
# print(Unique_Elements(list))


# Задача 4 (Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k)
def Make_Pol(degree):
    a = randint(0, 101)
    pol = (f'{a} * x ^ {degree} + ')
    i = degree - 1
    while i > 1:
        a = randint(0, 101)
        if a > 1:
            pol += (f'{a} * x ^ {i} + ')
        elif a == 1:
            pol += (f'x ^ {i} + ')
        i -= 1
    a = randint(0, 101)
    b = randint(0, 101)
    pol += (f'{a} * x + {b} = 0')
    return pol

# degree = int(input('Введите степень: '))

# file = open('file.txt', 'w')
# file.writelines(Make_Pol(degree))

# Задача 5 (Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов)
with open('file1.txt') as file1:
    pol1 = file1.read()
print(pol1)

# with open('file2.txt') as file2:
#     pol2 = file2.read()
# print(pol2)

pol1 = pol1.split(' ')
print(pol1)
