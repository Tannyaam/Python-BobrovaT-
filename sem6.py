# Задача 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# string_in = '12 + 24 - 2 * 4 + 4 / 2'
# string_in.split()

# f_sum = lambda num1, num2: num1 + num2
# f_sub = lambda num1, num2: num1 - num2
# f_mult = lambda num1, num2: num1 * num2 
# f_div = lambda num1, num2: num1 / num2

# for i in range(len(string_in)):
#     if string_in[i].isdigit():
#         string_in[i] = int(string_in[i])

# sum_and_sub = {'+': lambda num1, num2: num1 + num2,
#                '-': lambda num1, num2: num1 - num2}
# mult_and_div = {'*': lambda num1, num2: num1 * num2,
#                 '/': lambda num1, num2: num1 / num2}


# index = 0
# while ('*' in string_in) or ('/' in string_in):
#     if string_in[index] in mult_and_div:
#         temp = mult_and_div[string_in[index]](string_in[index-1], string_in[index+1])
#         del string_in[index - 1:index + 2] #удаляем элементы с index - 1 по index + 2б берет не включительно
#         string_in.insert(index - 1, temp)
#         index = 0
#     else: 
#         index += 1

# index = 0
# while ('+' in string_in) or ('-' in string_in):
#     if string_in[index] in sum_and_sub:
#         temp = sum_and_sub[string_in[index]](string_in[index-1], string_in[index+1])
#         del string_in[index - 1:index + 2] #удаляем элементы с index - 1 по index + 2б берет не включительно
#         string_in.insert(index - 1, temp)
#         index = 0
#     else: 
#         index += 1

# print(string_in)
# print(eval('12 + 24 - 2 * 4 + 4 / 2'))


# Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

# Задача 2. Дана последовательность чисел.Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = []
first_list = [1, 2, 3, 5, 1, 5, 3, 10]
# my_list = [i for i in first_list if first_list.count(i) == 1]

my_list = list(filter(lambda x: first_list.count(x) == 1, first_list))

print(my_list)