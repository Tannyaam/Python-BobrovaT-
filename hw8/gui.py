import csv

def action_request():
    action_number = int(input('Введите цифру, соответствующую действию,которое необходимо выполнить:\n1. Добавить контакт\n2. Удалить контакт\n3. Изменить контакт\n4. Найти контакт\n5. Показать все контакты\n'))
    return action_number

def return_phone_book():
    file = open('contacts.csv', 'r')
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        print('{:<15}{:<15}{:<15}{:<15}'.format(*row))