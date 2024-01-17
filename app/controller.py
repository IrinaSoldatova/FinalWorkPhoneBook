import text
import display
import model


def find_contact():
    word = display.input_data(text.input_search_word)
    result = model.find_contact(word)
    display.show_contacts(result, text.contacts_not_found(word))


def start_app():
    global contact
    while True:
        choice = display.main_menu()
        match choice:
            case 1:
                model.open_file()
                display.print_message(text.load_successful)
            case 2:
                if display.check_phone_book_opened():
                    contact = display.add_contact(text.new_contact)
                    model.make_contact(contact)
                    display.print_message(text.new_contact_added_successful([contact[0], contact[1]]))
            case 3:
                pb = model.phone_book
                display.show_contacts(pb, text.empty_phone_book)
            case 4:
                if display.check_phone_book_opened():
                    find_contact()
            case 5:
                if display.check_phone_book_opened():
                    find_contact()
                    pb = model.phone_book
                    while True:
                        c_id = display.input_valid_contact_id(text.input_id_change_contact)
                        c_contact = display.add_contact(text.change_contact, pb[c_id])
                        model.change_contact(c_id, c_contact)
                        display.print_message(text.contact_changed_successful([c_contact[0], c_contact[1]]))
                        break
            case 6:
                if display.check_phone_book_opened():
                    find_contact()
                    pb = model.phone_book
                    while True:
                        c_id = display.input_valid_contact_id(text.input_id_delete_contact)
                        name = model.delete_contact(c_id)
                        display.print_message(text.contact_deleted_successful(name))
                        break
            case 7:
                model.save_file()
                display.print_message(text.save_successful)
            case 8:
                display.print_message(text.good_bay)
                break
