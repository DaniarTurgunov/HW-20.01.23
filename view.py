
def main_menu():
    comands = ['Показать все контакты', 'Открыть файл', 'Сохранить файл', 'Новый контакт', 'Изменить контакт',
              'Удалить контакт', 'Найти контакт', 'Выйти из программы']
    print('\nВыберите пункт меню: ')
    for i in range(len(comands)):
        print(f'\t{i+1}. {comands[i]}')
    user_input = int(input('\nВведите пункт меню: '))
    return user_input

def show_contacts(phone_book:list):
    i = 1
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{i}. {item[0]} {item[1]} ({item[2]})')
            i+= 1
    else:
        print('Телефонная книга пустая или не загруженна')

def load_success():
    print('Телефонная книга загружена успешно')

def save_success():
    print('Телефонная книга сохраненна успешно')

def delete_success():
    print('Контакт успешно удален, изменения сохраненны')

def changes_success():
    print('Изменения прошли успешно и сохранены')

def pick_contact():
    pick_us = int(input('Выберите контакт: '))
    return pick_us

def new_contact():
    name = input('Введите Имя и Фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search

def delete_contact():
    delete_c = input('Введите данные которые хотите удалить: ')
    return delete_c

def diff_сontact():
    dif_c = int(input('Выберите какой параметр хотите изменить\n(имя = 1, номер = 2, комментарий = 3): '))
    while True:
        if 1<=dif_c<=3:
            break
        else:
            print('Нет такого параметра')
            dif_c = int(input('Выберите какой параметр хотите изменить\n(имя = 1, номер = 2, комментарий = 3): '))
    return dif_c

def parametr_c(parametr:int):
    match parametr:
        case 1:
            dif_c1 = input('Введите новое Имя и Фамилию контакта: ')
            return dif_c1
        case 2:
            dif_c2 = input('Введите новый номер телефона: ')
            return dif_c2
        case 3:
            dif_c3 = input('Введите новый комментарий: ')   
            return dif_c3
    