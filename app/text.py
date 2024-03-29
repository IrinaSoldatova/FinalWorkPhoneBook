menu_text = ['Главное меню',
             'Открыть телефонный справочник',
             'Создать контакт',
             'Показать контакты',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Сохранить изменения',
             'Выход из телефонного справочника']

menu_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно загружена!'

save_successful = 'Телефонная книга успешно сохранена!'

empty_phone_book = 'Телефонная книга пуста или не открыта!'

new_contact = ['Введите фамилию: ',
               'Введите имя: ',
               'Введите номер телефона: ',
               'Введите комментарий: ']


def new_contact_added_successful(name: list) -> str:
    return f'Контакт {' '.join(name)} успешно добавлен!'


input_search_word = 'Введите данные контакта для поиска: '


def contacts_not_found(word: str) -> str:
    return f'Контакт с данными {word} не найден!'


input_id_change_contact = 'Введите ID контакта, который хотите изменить или 0, чтобы вернуться в главное меню: '

change_contact = ['Введите новую фамилию или оставьте без изменений: ',
                  'Введите новое имя или оставьте без изменений: ',
                  'Введите новый номер телефона или оставьте без изменений: ',
                  'Введите новый комментарий или оставьте без изменений: ']


def contact_changed_successful(name: list) -> str:
    return f'Контакт {' '.join(name)} успешно изменен!'


invalid_contact_id_message = 'Некорректный ID контакта, попробуйте еще раз.'

input_id_delete_contact = 'Введите ID контакта, который хотите удалить или 0, чтобы вернуться в главное меню: '


def contact_deleted_successful(name: list) -> str:
    return f'Контакт {' '.join(name)} успешно удален!'


good_bye = 'До новых вcтреч!'
