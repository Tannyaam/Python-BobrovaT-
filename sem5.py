# Задача 1 (В файле находится N натуральных чисел, записаных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число)

# with open('file_sem5.txt') as file:
#     arr = file.read()
# arr = list(map(int, arr.split()))

# for i in range(1, len(arr)):
#     if arr[i] - 1 != arr[i-1]:
#         search_num = arr[i] - 1

# list = [arr[i] - 1 for i in range(1, len(arr)) if arr[i] - 1 != arr[i-1]]
# print(list)


# Задача 2 (Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# def Increase_arr(arr):
#     arr_incr = []
#     len_arr_incr = 0
#     arr_incr.append(arr[0])
#     for i in range(1, len(arr)):
#         if arr[i] > arr[len_arr_incr]:
#             arr_incr.append(arr[i])
#             len_arr_incr += 1
#     return arr_incr

# arr = [1, 5, 2, 3, 4, 6, 1, 7]
# print(Increase_arr(arr))

# list = ([arr[i] for i in range(1, len(arr)) if arr[i] > max(arr[0:i])])
# list.insert(0, arr[0])
# print(list)

# Задача 3 (Напишите программу, удаляющую из текста все слова, содержащие "абв")
# 'Мы неабв очень любим Питон иабв Джавабв' => 'Мы очень любим Питон'

phrase = 'Мы неабв очень любим Питон иабв Джавабв'
search_phrase = 'абв'
list_phrase = phrase.split(' ')
# i = 0

# while i in range(len(list_phrase)):
#     if search_phrase in list_phrase[i]:
#         list_phrase.remove(list_phrase[i])
#     else:
#         i += 1

# print(list_phrase)

final_phrase = [item for item in list_phrase if search_phrase not in item]
print(final_phrase)