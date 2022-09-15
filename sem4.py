# Задача 1 (Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел)
def Find_Max_And_Min(list):
    max = list[0]
    min = list[0]
    for i in list[1:]:
        if i > max:
            max = i
        elif i < min:
            min = i
    return min, max

# list = input('Задайте набор чисел: ').split(' ')
# print(Find_Max_And_Min(list))

# Встроенная функция:

# max_num = max(list)
# print('Максимальный элемент - ', max_num)
# min_num = min(list)
# print('Минимальный элемент - ', min_num)


# Задача 2 (Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 1) с помощью математических формул нахождения корней квадратного уравнения 2) с помощью дополнительных библиотек Python)
def Find_x(a, b, c):
    dis = pow(b, 2) - 4 * a * c
    if dis >= 0:
        x1 = ((- b) + pow(dis, 0.5)) / (2 * a)
        x2 = ((- b) - pow(dis, 0.5)) / (2 * a)
        return x1, x2
    return None

# a = int(input('Задайте коэффициенты квадратного уравнения (аx² + bx + c): а = '))
# b = int(input('b = '))
# c = int(input('c = '))
# print(Find_x(a, b, c))

# Задача 3 (Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел. Ответ записать в файл)
def Find_Nok(num1, num2):
    max_num = max(num1, num2)
    for i in range(max_num, num1*num2):
        if (i % num1 == 0) and (i % num2 == 0):
            return i
            break
    return num1*num2

num1 = int(input('Введите первое число '))
num2 = int(input('Введите второе число '))
list = str(Find_Nok(num1, num2))
file = open('file.txt', 'w')
file.writelines(list)