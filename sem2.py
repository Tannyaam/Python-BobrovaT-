# i = 1

# while i <= 10:
#     print(i, end='')
#     i += 1


# Задача 1 (Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов)

from turtle import st


n = int(input('Введите число N: '))

array = [1]
i = 1

while i < n:
    array.append(array[i-1] * (-3))
    i +=1

print(f"{array}, ")

#или

i = 0
while i < n:
    print(f"{i + 1}: {(-3) ** i} ")
    i += 1



# Задача 2 (Для натурального n создать последовательности 3n + 1)

# n = int(input('Введите число N: '))

# array = []
# i = 1

# while i <= n:
#     array.append(3 * i + 1)
#     print(f"{i}: {array[i-1]}")
#     i +=1


# Задача 3 (Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой)


# str = input('Введите строку: ')
# str_2 = input('Введите искомую подстроку: ')

# len_str_2 = len(str_2)
# i = 0
# matching = 0

# while i < len(str):
#     check_1 = 1
#     if str[i] == str_2[0]:
#         j = i + 1
#         k = 1
#         for j in range(j + len_str_2):
#             if (k < len_str_2) and (str[j] == str_2[k]):
#                 check_1 += 1
#                 k += 1
#     if check_1 == len_str_2:
#         matching += 1
#     i += 1

# print(matching)

str = input('Введите строку: ')
str_2 = input('Введите искомую подстроку: ')
count = 0

for i in range(0, len(str) - len(str_2)):
    if str_2 == str[i:i + len(str_2)]:
        count += 1

#или

str = input('Введите строку: ')
str_2 = input('Введите искомую подстроку: ')

result = str.count(str_2)