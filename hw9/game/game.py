# Задача 3 (Создайте программу для игры в ""Крестики-нолики"")

import emoji

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
            print(emoji.emojize('Второй игрок выиграл :partying_face:'))
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
            print(emoji.emojize('Первый игрок выиграл :partying_face:'))
            exit()
    if turn_number == 9:
        print('Ничья, игра окончена :skull_and_crossbones:')