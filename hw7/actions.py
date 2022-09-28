import gui

def add_new_contact():
    file = open('contacts.txt', 'a')
    new_contact = input('Введите фамилию контакта: ')
    new_contact += ', '
    new_contact += input('Введите имя контакта: ')
    new_contact += ', '
    new_contact += input('Введите телефон контакта: ')
    new_contact += ', '
    new_contact += input('Введите описание контакта: ')
    file.writelines(f'\n{new_contact}')

def delete_contact():
    all_contacts = gui.return_phone_book()
    input_contact = input('Введите фамилию контакта, который нужно удалить: ')
    for i in range(len(all_contacts)):
        if input_contact in all_contacts[i]:
            all_contacts.remove(all_contacts[i])
            break
    file = open('contacts.txt', 'w')
    # file.writelines('')
    # file = open('contacts.txt', 'a')
    for i in range(len(all_contacts)):
        file.writelines(f'{all_contacts[i]}\n')
    
def change_information ():
    all_contacts = gui.return_phone_book()
    input_contact = input('Введите фамилию контакта, который нужно изменить: ')
    for i in range(len(all_contacts)):
        if input_contact in all_contacts[i]:
            all_contacts.remove(all_contacts[i])
            break
    file = open('contacts.txt', 'w')
    # file.writelines('')
    # file = open('contacts.txt', 'a')
    new_contact = input('Введите фамилию контакта: ')
    new_contact += ', '
    new_contact += input('Введите имя контакта: ')
    new_contact += ', '
    new_contact += input('Введите телефон контакта: ')
    new_contact += ', '
    new_contact += input('Введите описание контакта: ')
    file.writelines(f'{new_contact}')
    for i in range(len(all_contacts)):
        file.writelines(f'\n{all_contacts[i]}')

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