import gui
import csv

def add_new_contact():
    surname = input('Введите фамилию контакта: ')
    name = input('Введите имя контакта: ')
    phone_num = input('Введите телефон контакта: ')
    contact_info = input('Введите описание контакта: ')
    new_contact = [surname, name, phone_num, contact_info]
    with open('contacts.csv', 'a') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(new_contact)

def delete_contact():
    gui.return_phone_book()
    input_contact = input('Введите фамилию контакта, который нужно удалить: ')
    file = open('contacts.csv', 'r')
    reader = csv.reader(file, delimiter = ';')
    reader2 = []
    for row in reader:
        if input_contact != row[0]:
            reader2.append(row)
    file = open('contacts.csv', 'w')
    for row in reader2:
        writer = csv.writer(file, delimiter = ';', lineterminator = '\r')
        writer.writerow(row)
    
def change_information ():
    gui.return_phone_book()
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
    for row in reader2:
        writer = csv.writer(file, delimiter = ';', lineterminator = '\r')
        writer.writerow(row)

def find_contact():
    file = open('contacts.csv', 'r')
    reader = csv.reader(file, delimiter = ';')
    input_contact = input('Введите фамилию контакта, который нужно найти: ')
    for row in reader:
        if row[0] == input_contact:
            print('{:<15}{:<15}{:<15}{:<15}'.format(*row))

def show_all():
    file = open('contacts.csv', 'r')
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        print('{:<15}{:<15}{:<15}{:<15}'.format(*row))    

def action_selection(action_number):
    if action_number == 1:
        act = add_new_contact()
    elif action_number == 2:
        act = delete_contact()
    elif action_number == 3:
        act = change_information()
    elif action_number == 4:
        act = find_contact()
    elif action_number == 5:
        act = show_all()
    return act