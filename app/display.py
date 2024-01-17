import model
import text
import controller


def main_menu() -> int:
    for n, item in enumerate(text.menu_text):
        if n == 0:
            print(item)
        else:
            print(f'\t{n}.{item}')
    while True:
        choice = input(text.menu_choice)
        if choice.isdigit() and 0 < int(choice) < len(text.menu_text):
            return int(choice)
        print(f'Введите пункт меню от 1 до {len(text.menu_text) - 1}')


def show_contacts(p_book: dict[int, list[str]], error_message: str):
    max_size = list(map(lambda x: len(max(x, key=len)), list(zip(*p_book.values()))))
    if p_book:
        print('\n' + '#' * (sum(max_size) + 10))
        for n, contact in p_book.items():
            print(f'{n:>3}. {contact[0]:<{max_size[0]}} {contact[1]:<{max_size[1]}}'
                  f' {contact[2]:<{max_size[2]}} {contact[3]:<{max_size[3]}}')
        print('#' * (sum(max_size) + 10) + '\n')
    else:
        print_message(error_message)


def print_message(message: str):
    print('\n' + '#' * len(message))
    print(message)
    print('#' * len(message) + '\n')


def add_contact(message: list[str], contact: list[str] = None):
    contact = contact if contact else ['', '', '', '']
    for n, mes in enumerate(message):
        field = input(mes)
        contact[n] = field if field else contact[n]
    return contact


def input_data(message: str) -> str:
    return input(message)


def input_valid_contact_id(promt):
    while True:
        c_id = input_data(promt)
        if c_id == '0':
            controller.start_app()
        if not c_id.isdigit():
            print_message(text.invalid_contact_id_message)
            continue
        c_id = int(c_id)
        if c_id not in range(1, len(model.phone_book) + 1):
            print_message(text.invalid_contact_id_message)
            continue
        return c_id


def check_phone_book_opened():
    if not model.phone_book:
        print_message(text.empty_phone_book)
        return False
    return True
