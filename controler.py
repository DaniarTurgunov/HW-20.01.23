import view
import model

def start():
    user_choice = 0
    while user_choice != 8:    
        user_choice = view.main_menu()

        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)
                pick_us = view.pick_contact()
                result_f = list(model.pick_contact(result,pick_us))
                parametr = view.diff_сontact()
                pr = view.parametr_c(parametr)
                c = list(model.dif_contact(result_f, parametr, pr))
                model.update_phone_book(c)
                model.delete_contact(search)
                model.save_phone_book()
                view.changes_success()
                
            case 6:
                delete_c = view.delete_contact()
                model.delete_contact(delete_c)
                model.save_phone_book()
                view.delete_success()
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)

