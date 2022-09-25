# Задача 1 (Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции)
# input_arr = [1, 8, 3, 4, 5]
# input_arr = [input_arr[i] for i in range(len(input_arr)) if i % 2 != 0]
# print(input_arr)
# sum = 0
# for i in input_arr:
#     sum += i
# print(sum)



# Задача 2 (Напишите программу, удаляющую из текста все слова, содержащие ""абв")
# text = 'Напишите программу кемабв, удаляющую абв из текста неабв все слова'
# search_text = 'абв'
# text_list = text.split()

# final_text = list(filter(lambda text_list: search_text not in text_list, text_list))
# print(final_text)



# Задача 3 (Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму)
k = int(input('Введите число k: '))
sum = 0

arr = [round(((1 + 1 / i) ** i), 3) for i in range(1, k + 1)]
for i in arr:
    sum += i
print(arr)
print(sum)