# Задача 1 (Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным)

num = int(input('Введите цифру, соответствующую дню недели '))
if (num == 6) or (num == 7):  # if num == (6 or 7)
     print(f'Это выходной день')
else:
     print(f'Это будний день')

# Задача 2 (Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат)

a = int(input('Введите a '))
y = int(input('Введите y '))
z = int(input('Введите z '))
if (a == 1 or y == 1 or z == 1):
    print(False)
else:
    print(True)

# a  b  c  1  2
# 0  0  0  1  1
# 0  0  1  0  0
# 0  1  0  0  0
# 0  1  1  0  0
# 1  0  0  0  0
# 1  0  1  0  0
# 1  1  0  0  0
# 1  1  1  0  0

# Задача 3 (Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится))

coor_x = int(input('Введите x '))
coor_y = int(input('Введите y '))
if (coor_x >= 0):
    if (coor_y >= 0):
        print('Точка находится в первой четверти')
    else:
        print('Точка находится в четвертой четверти')
else:
    if (coor_y >= 0):
        print('Точка находится во второй четверти')
    else:
        print('Точка находится в третьей четверти')

# Задача 4 (Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y))

num = int(input('Введите номер четверти '))
if (num == 1):
    print('(x >= 0) и (y >= 0)')
elif (num == 2):
    print('(x <= 0) и (y >= 0)')
elif (num == 3):
    print('(x <= 0) и (y <= 0)')
elif (num == 4):
    print('(x >= 0) и (y <= 0)')

# Задача 5 (Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве)

from math import sqrt


coor_x1 = int(input('Введите координату x первой точки '))
coor_y1 = int(input('Введите координату y первой точки '))
coor_x2 = int(input('Введите координату x второй точки '))
coor_y2 = int(input('Введите координату y второй точки '))
length_2 = ((coor_x1 - coor_x2)*(coor_x1 - coor_x2) + (coor_y1 - coor_y2)*(coor_y1 - coor_y2))
length = sqrt(length_2)
print(round(length,3))

