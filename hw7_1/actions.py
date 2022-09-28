import gui

def add_new_contact():
    file = open('contacts.txt', 'a')
    new_contact = input('Введите фамилию контакта: ')
    new_contact += input('Введите имя контакта: ')
    new_contact += '\n'
    new_contact += input('Введите телефон контакта: ')
    new_contact += '\n'
    new_contact += input('Введите описание контакта: ')
    file.writelines(f'\n{new_contact}')

def delete_contact():
    gui.return_phone_book
    input_contact = input('Введите фамилию контакта, который нужно удалить: ')
    for i in range(len(gui.all_contacts)):
        if gui.all_contacts[i] == input_contact:
            gui.all_contacts.remove(gui.all_contacts[i])
            break
    file = open('contacts.txt', 'w')
    file.writelines('')
    file = open('contacts.txt', 'a')
    for i in range(len(gui.all_contacts)):
        file.writelines('\n')
        file.writelines(f'{gui.all_contacts[i]}')
    
def change_information ():
    gui.return_phone_book
    input_contact = input('Введите фамилию контакта, который нужно изменить: ')
    for i in range(len(gui.all_contacts)):
        if input_contact in gui.all_contacts[i]:
            gui.all_contacts.remove(gui.all_contacts[i])
            break
    file = open('contacts.txt', 'w')
    file.writelines('')
    file = open('contacts.txt', 'a')
    new_contact = input('Введите фамилию контакта: ')
    new_contact += ', '
    new_contact += input('Введите имя контакта: ')
    new_contact += ', '
    new_contact += input('Введите телефон контакта: ')
    new_contact += ', '
    new_contact += input('Введите описание контакта: ')
    file.writelines(f'{new_contact}')
    for i in range(len(gui.all_contacts)):
        file.writelines('\n')
        file.writelines(f'{gui.all_contacts[i]}')

def find_contact():
    file = open('contacts.txt', 'r')
    all_contacts = list(file.read().split('\n'))
    input_contact = input('Введите фамилию контакта, который нужно найти: ')
    contact = list(filter(lambda x: input_contact in x, all_contacts))
    print(''.join(contact))

def action_selection(action_number):
    if action_number == 1:
        act = add_new_contact()
    elif action_number == 2:
        act = delete_contact()
    elif action_number == 3:
        act = change_information()
    elif action_number == 4:
        act = find_contact()
    return act