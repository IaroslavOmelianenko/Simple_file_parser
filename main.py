# открыть файл
def open_file(filename):
    contacts = {}
    with open(filename, 'r') as file:
        for line in file:
            name, number, comment = line.strip().split(',')
            contacts[name] = {'number': number, 'comment': comment}
    return contacts


# сохранить файл
def save_file(filename, contacts):
    with open(filename, 'w') as file:
        for name, data in contacts.items():
            number = data['number']
            comment = data['comment']
            file.write(f'{name},{number},{comment}\n')


# показать все контакты
def show_contacts(contacts):
    for name, data in contacts.items():
        print(f'{name}: {data["number"]} ({data["comment"]})')


# добавить контакт
def add_contact(contacts, name, number, comment):
    if name not in contacts:
        contacts[name] = {'number': number, 'comment': comment}
        print(f'Контакт {name} добавлен')
    else:
        print(f'Контакт {name} уже существует')


# найти контакт
def find_contact(contacts, name):
    if name in contacts:
        data = contacts[name]
        print(f'{name}: {data["number"]} ({data["comment"]})')
    else:
        print(f'Контакт {name} не найден')


# изменить контакт
def edit_contact(contacts, name, new_number, new_comment):
    if name in contacts:
        data = contacts[name]
        data['number'] = new_number
        data['comment'] = new_comment
        print(f'Контакт {name} изменен')
    else:
        print(f'Контакт {name} не найден')


# удалить контакт
def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f'Контакт {name} удален')
    else:
        print(f'Контакт {name} не найден')


# меню и запуск
def main():
    filename = 'phonebook.txt'
    contacts = open_file(filename)

    while True:
        print('Выберите действие:')
        print('1 - показать все контакты')
        print('2 - добавить контакт')
        print('3 - найти контакт')
        print('4 - изменить контакт')
        print('5 - удалить контакт')
        print('0 - выход')

        choice = input()

        if choice == '1':
            show_contacts(contacts)
        elif choice == '2':
            name = input('Введите имя контакта: ')
            number = input('Введите номер телефона: ')
            comment = input('Введите комментарий: ')
            add_contact(contacts, name, number, comment)
            save_file(filename, contacts)
        elif choice == '3':
            name = input('Введите имя контакта: ')
            find_contact(contacts, name)
        elif choice == '4':
            name = input('Введите имя контакта: ')
            new_number = input('Введите новый номер: ')
            new_comment = input('Введите новый комментарий: ')
            edit_contact(contacts, name, new_number, new_comment)
            save_file(filename, contacts)
        elif choice == '5':
            name = input('Введите имя контакта: ')
            delete_contact(contacts, name)
            save_file(filename, contacts)
        elif choice == '0':
            break
        else:
            print('Неправильный выбор. Выберите действие от 0 до 5')

main()