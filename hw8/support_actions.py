import csv
import user_choice
import gui

def return_phone_book():
    file = open('contacts.csv', 'r')
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        if row != '':
            print('{:<15}{:<15}{:<15}{:<15}'.format(*row))
