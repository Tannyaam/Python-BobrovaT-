# Задача 1 ( Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел)
# import time

# for i in range(10):
#     a = time.time()
#     print(int(a*1000000)%100)



# Задача 2 (Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число)
str = input('Задайте список: ').split(' ')
# for i in range(len(str)):
#     for j in str[i]:
#         if j == '7':
#             print(str[i])
#             break
for i in str:
    if i.find('7') >= 0:
        print(i)
    else:
        print('none')


# Задача 3 (Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет)
str = input('Задайте список: ').split(' ')
str_2 = input('Задайте искомую строку: ')
# index = 0
# search_index = 0
# for i in str:
#     if (i == str_2) and (index != 0):
#         search_index = index
#         break
#     index += 1
# if search_index == 0:
#     print(-1)
# else:
#     print(search_index)

# или
count = 0
for i in range(len(str)):
    if str[i] == str_2:
        count += 1
        if count == 2:
            print(i)