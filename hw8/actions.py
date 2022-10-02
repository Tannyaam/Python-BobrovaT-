import gui
import csv
import support_actions

def add_new_contact():
    surname = input('Введите фамилию контакта: ')
    name = input('Введите имя контакта: ')
    phone_num = input('Введите телефон контакта: ')
    contact_info = input('Введите описание контакта: ')
    new_contact = [surname, name, phone_num, contact_info]
    with open('contacts.csv', 'a') as file:
        writer = csv.writer(file, delimiter = ';', lineterminator = '\r')
        writer.writerow(new_contact)

def delete_contact():
    support_actions.return_phone_book()
    input_contact = input('Введите фамилию контакта, который нужно удалить: ')
    file = open('contacts.csv', 'r')
    reader = csv.reader(file, delimiter = ';')
    reader2 = []
    for row in reader:
        if input_contact != row[0]:
            reader2.append(row)
    file = open('contacts.csv', 'w')
    writer = csv.writer(file, delimiter = ';', lineterminator = '\r')
    writer.writerows(reader2)
    print('\nКонтакт удален\n')
    
def change_information ():
    support_actions.return_phone_book()
    input_contact = input('Введите фамилию контакта, который нужно изменить: ')
    file = open('contacts.csv', 'r')
    reader = csv.reader(file, delimiter = ';')
    reader2 = []
    for row in reader:
        if input_contact != row[0]:
            reader2.append(row)
    surname = input('Введите фамилию контакта: ')
    name = input('Введите имя контакта: ')
    phone_num = input('Введите телефон контакта: ')
    contact_info = input('Введите описание контакта: ')
    new_contact = [surname, name, phone_num, contact_info]
    reader2.append(new_contact)
    file = open('contacts.csv', 'w')
    writer = csv.writer(file, delimiter = ';', lineterminator = '\r')
    writer.writerows(reader2)
    print('\nКонтакт успешно изменен\n')

def find_contact():
    file = open('contacts.csv', 'r')
    reader = csv.reader(file, delimiter = ';')
    input_contact = input('Введите фамилию контакта, который нужно найти: ')
    for row in reader:
        if row[0] == input_contact:
            print('{:<15}{:<15}{:<15}{:<15}'.format(*row))
            break

def show_all():
    file = open('contacts.csv', 'r')
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        print('{:<15}{:<15}{:<15}{:<15}'.format(*row))    