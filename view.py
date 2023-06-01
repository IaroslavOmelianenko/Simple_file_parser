import text


def main_menu() -> int:
    print(text.main_menu)
    choice = input(text.input_choice)
    return choice

def show_contacts(contacts):
    for name, data in contacts.items():
        print(f'{name}: {data["number"]} ({data["comment"]})')

def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')