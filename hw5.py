# Задача 1 (Напишите программу, удаляющую из текста все слова, содержащие ""абв")
# text = 'Напишите программу кемабв, удаляющую абв из текста неабв все слова'
# search_text = 'абв'
# text_list = text.split()

# final_text = [item for item in text_list if search_text not in item]
# print(final_text)



# Задача 2 (Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?)

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

# turn_num = randint(1, 2)
# # print(f"Первым ходит игрок {turn_num}.")
# n = 2021
# while n > 0:
    # if turn_num % 2 == 0:
    #     turn_player_2 = int(input('Игрок 2: введите количество конфет: '))
    #     while (turn_player_2 > 28) or (turn_player_2 < 1):
    #         print('Введенное количество не соответствует условиям. Введите заново.')
    #         turn_player_2 = int(input('Игрок 2: введите количество конфет: '))
    #     n -= turn_player_2
    # else:
    #     turn_player_1 = int(input('Игрок 1: введите количество конфет: '))
    #     while (turn_player_1 > 28) or (turn_player_1 < 1):
    #         print('Введенное количество не соответствует условиям. Введите заново.')
    #         turn_player_1 = int(input('Игрок 1: введите количество конфет: '))
    #     n -= turn_player_1
    # print(f"Остальсь {n} конфет")
    # if (n == 0) and (turn_num % 2 == 0):
    #     print('Выиграл 2 игрок')
    # elif (n == 0) and (turn_num % 2 != 0):
    #     print('Выиграл 1 игрок')
    # turn_num += 1

# игра с ботом:

# n = 108
# turn_num = randint(1, 2)
# if turn_num == 1:
#     print(f"Вы ходите первый.")
# else:
#     print(f"Первым ходит компьютер.")
# while n > 0:
#     if turn_num % 2 == 0:
#         turn_player_2 = randint(1, 28)
#         if n == 28:
#             turn_player_2 = 28
#         print(f"Компьютер: количество конфет: {turn_player_2}")
#         n -= turn_player_2
#     else:
#         turn_player_1 = int(input('Введите количество конфет: '))
#         while (turn_player_1 > 28) or (turn_player_1 < 1):
#             print('Введенное количество не соответствует условиям. Введите заново.')
#             turn_player_1 = int(input('Введите количество конфет: '))
#         n -= turn_player_1
#     print(f"Осталось {n} конфет")
#     if (n == 0) and (turn_num % 2 == 0):
#         print('Выиграл компьютер')
#     elif (n == 0) and (turn_num % 2 != 0):
#         print('Вы выиграли')
#     turn_num += 1

# Задача 3 (Создайте программу для игры в ""Крестики-нолики"")
pole = str('| 1 | 2 | 3 |\n-------------\n| 4 | 5 | 6 |\n-------------\n| 7 | 8 | 9 |')
index_1 = pole.find('1')
index_2 = pole.find('2')
index_3 = pole.find('3')
index_4 = pole.find('4')
index_5 = pole.find('5')
index_6 = pole.find('6')
index_7 = pole.find('7')
index_8 = pole.find('8')
index_9 = pole.find('9')
player_1 = 'X'
player_2 = '0'
print(pole)


def First_player_turn(pole):
    print('Игрок 1: Укажите номер ячейки, соответствующий вашему ходу: ')
    turn = input()
    player_1 = 'X'
    for i in range(len(pole)):
        if pole[i] == turn:
            pole = pole.replace(pole[i], player_1)
            break
    print(pole)
    return str(pole)

def Second_player_turn(pole):
    print('Игрок 2: Укажите номер ячейки, соответствующий вашему ходу: ')
    turn = input()
    player_2 = '0'
    for i in range(len(pole)):
        if pole[i] == turn:
            pole = pole.replace(pole[i], player_2)
            break
    print(pole)
    return pole

for turn_number in range(1, 10):
    if turn_number % 2 == 0 :
        pole = Second_player_turn(pole)
        if ((pole[index_1] == pole[index_2] == pole[index_3] == '0') 
        or (pole[index_4] == pole[index_5] == pole[index_6] == '0') 
        or (pole[index_7] == pole[index_8] == pole[index_9] == '0')
        or (pole[index_1] == pole[index_4] == pole[index_7] == '0')
        or (pole[index_2] == pole[index_5] == pole[index_8] == '0')
        or (pole[index_3] == pole[index_6] == pole[index_9] == '0')
        or (pole[index_1] == pole[index_5] == pole[index_9] == '0')
        or (pole[index_3] == pole[index_5] == pole[index_7] == '0')):
            print('Второй игрок выиграл')
            exit()
    else:
        pole = First_player_turn(pole)
        if ((pole[index_1] == pole[index_2] == pole[index_3] == 'X') 
        or (pole[index_4] == pole[index_5] == pole[index_6] == 'X') 
        or (pole[index_7] == pole[index_8] == pole[index_9] == 'X')
        or (pole[index_1] == pole[index_4] == pole[index_7] == 'X')
        or (pole[index_2] == pole[index_5] == pole[index_8] == 'X')
        or (pole[index_3] == pole[index_6] == pole[index_9] == 'X')
        or (pole[index_1] == pole[index_5] == pole[index_9] == 'X')
        or (pole[index_3] == pole[index_5] == pole[index_7] == 'X')):
            print('Первый игрок выиграл')
            exit()
    if turn_number == 9:
        print('Ничья, игра окончена')


# Задача 4 (Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах)
# str_ing = 'aaaaaabbbbccdeeeefff'
# str_f = ""

# file = open('file_hw5.txt', 'r')
# str_ing = file.read()
# file2 = open('file2_hw5.txt', 'w')

# str_f = ''
# i = 0
# while i < len(str_ing):
#     j = i + 1
#     count = 1
#     search_char = str_ing[i]
#     while (j < len(str_ing)) and (str_ing[j] == search_char):
#         count += 1
#         j += 1
#     if count > 0:
#         i += count
#     else:
#         i += 1
#     str_f = str_f + search_char + str(count)

# file2.writelines(str_f)