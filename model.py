import text


class PhoneBook:

    def open_file(self):
        contacts = {}
        with open(text.phonebook_filename, 'r') as file:
            for line in file:
                name, number, comment = line.strip().split(',')
                contacts[name] = {'number': number, 'comment': comment}
        return contacts


    def save_file(filename, contacts):
        with open(filename, 'w') as file:
            for name, data in contacts.items():
                number = data['number']
                comment = data['comment']
                file.write(f'{name},{number},{comment}\n')


    def add_contact(contacts, name, number, comment):
        if name not in contacts:
            contacts[name] = {'number': number, 'comment': comment}
            text.contact_saved(name)
        else:
            text.contact_already_exist(name)


    def find_contact(contacts, name):
        if name in contacts:
            data = contacts[name]
            print(f'{name}: {data["number"]} ({data["comment"]})')
        else:
            text.contact_not_exist(name)

    def edit_contact(contacts, name, new_number, new_comment):
        if name in contacts:
            data = contacts[name]
            data['number'] = new_number
            data['comment'] = new_comment
            text.contact_updated(name)
        else:
            text.contact_not_exist(name)

    def delete_contact(contacts, name):
        if name in contacts:
            del contacts[name]
            text.contact_deleted(name)
        else:
            text.contact_not_exist(name)
