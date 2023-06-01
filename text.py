# -*- coding: utf-8 -*-

main_menu = '''\nМеню:
    1 - показать все контакты
    2 - добавить контакт
    3 - найти контакт
    4 - изменить контакт
    5 - удалить контакт
    0 - выход\n'''

input_choice = 'Выберите действие:'
input_name = 'Введите имя контакта:'
input_phone_number = 'Введите номер телефона:'
input_comment = 'Введите комментарий:'
input_new_phone_number = 'Введите новый номер контакта:'
input_new_comment = 'Введите новый комментарий:'
wrong_choice = 'Неправильный выбор. Выберите действие от 0 до 5'

list_of_contacts = 'Список контактов:'
exit = 'Выход'

phonebook_filename = 'phonebook.txt'

def contact_add_success(name: str):
    return print(f'Контакт {name} добавлен')

def contact_already_exist(name: str):
    return print(f'Контакт {name} уже существует')

def contact_not_exist(name: str):
    return print(f'Контакт {name} не найден')

def contact_updated(name: str):
    return print(f'Контакт {name} изменен')

def contact_deleted(name: str):
    return f'Контакт {name} удален'
