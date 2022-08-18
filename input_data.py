def new_contact():
    first_name = input('Введите имя -> ')
    last_name = input('Введите фамилию -> ')
    phone_number = input('Введите телефонный номер -> ')
    comment = input('Введите комментарий -> ')
    mem = {'Фамилия': last_name, 'Имя': first_name, 'Телефонный номер': phone_number, 'Комментарий': comment}
    return mem

def first_vvod():
    vvod = input('Хотите создать новую книгу? Y/N-> ')
    if vvod == 'Y' or vvod == 'y':
        return True
    elif vvod == 'N' or vvod == 'y':
        return False
    else:
        print('Неверный ввод')
        return first_vvod()

def vibor():
    vvod = input('1. Создать телефонную книгу\n2. Добавить новый контакт\n3. Удалить контакт\n4. Показать все контакты\n5. Найти контакт\n-> ')
    return(vvod)


def delete_vibor():
    vvod = input('1. Удаление по индексу\n2. Удаление по фамилии\n-> ')
    return vvod

def delete_vvod(par):
    vvod = input(f'Введите {par} -> ')
    return vvod

def find_vibor():
    vvod = input('1. Поиск по фамилии\n2. Поиск по имени\n3. Поиск по номеру телефона\n4. Поиск по комментарию\n-> ')
    return vvod

def find_vvod(par):
    vvod = input(f'Введите {par} -> ')
    return vvod