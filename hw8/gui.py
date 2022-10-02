import csv

def action_request():
    action_number = int(input('Введите цифру, соответствующую действию,которое необходимо выполнить:\n1. Добавить контакт\n2. Удалить контакт\n3. Изменить контакт\n4. Найти контакт\n5. Показать все контакты\n'))
    return action_number

def continue_work():
    action_number = int(input('Продолжить работу с книгой или завершить?\n1. Продолжить\n2. Завершить\n'))
    return action_number
