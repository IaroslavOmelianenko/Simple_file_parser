import text
import view
import model


def start():
    while True:
        choice = view.main_menu()
        phonebook = model.PhoneBook
        contacts = phonebook.open_file(text.phonebook_filename)

        if choice == '1':
            view.print_message(text.list_of_contacts)
            view.show_contacts(contacts)

        elif choice == '2':
            name = input(text.input_name)
            number = input(text.input_phone_number)
            comment = input(text.input_comment)
            phonebook.add_contact(contacts, name, number, comment)
            phonebook.save_file(text.phonebook_filename, contacts)

        elif choice == '3':
            name = input(text.input_name)
            phonebook.find_contact(contacts, name)

        elif choice == '4':
            name = input(text.input_name)
            new_number = input(text.input_new_phone_number)
            new_comment = input(text.input_new_comment)
            phonebook.edit_contact(contacts, name, new_number, new_comment)
            phonebook.save_file(text.phonebook_filename, contacts)

        elif choice == '5':
            name = input(text.input_name)
            phonebook.delete_contact(contacts, name)
            phonebook.save_file(text.phonebook_filename, contacts)
        elif choice == '0':
            view.print_message(text.exit)
            break
        else:
            print(text.wrong_choice)
