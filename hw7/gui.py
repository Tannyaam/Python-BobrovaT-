def action_request():
    action_number = int(input('Введите цифру, соответствующую действию, которое необходимо выполнить:\n1. Добавить конктакт\n2. Удалить контакт\n3. Изменить контакт\n4. Найти контакт\n'))
    return action_number

def return_phone_book():
    file = open('contacts.txt', 'r')
    all_contacts = list(file.read().split('\n'))
    print('Фамилия, имя, телефон, описание:')
    for i in range(len(all_contacts)):
        print(all_contacts[i])
    return all_contacts