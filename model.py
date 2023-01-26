phone_book = []
path = r'C:\Users\tbyla\OneDrive\Рабочий стол\GB_Python\practic 20.01.23\Phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def update_phone_book(contact:list):
    global phone_book
    phone_book.append(contact)

def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))

def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line)) 
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))
     
def search_contact(search: str):
    global phone_book
    search_result = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_result.append(line)
                break
    return search_result

def delete_contact(delete_c: str):
    global phone_book
    for line in phone_book:
        for field in line:
            if delete_c in field:
                phone_book.remove(line)
                break

def dif_contact(result_f:list, parametr: int, pr: str):
    pr1 = []
    for x in result_f:
        pr1.append(x)
    for i in range(len(pr1)):
        if parametr == 1:
            pr1[0] = str(pr)
            break        
        elif parametr == 2:
            pr1[1] = str(pr)
            break  
        elif parametr == 3:
            pr1[2] = str(pr)
            break  
    return pr1
    
def pick_contact(result: list, pick_us: int):
    if len(result) > 1:
        for i in range(len(result)):
            if pick_us-1 == i:
                return result[i]
    else:
        return result[0]


    