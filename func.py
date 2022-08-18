import pandas as pd
import input_data as id
import output_data as od

def create_new_book():
    phone_book = create()
    print('Создайте первый контакт')
    add_number(phone_book)

def create():
    return pd.DataFrame({'Фамилия':[], 'Имя': [], 'Телефонный номер': [], 'Комментарий': []})

def add_number(phone_book):
    mem = id.new_contact()
    phone_book = phone_book.append(mem,ignore_index=True)
    phone_book.to_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_7/data.csv', index=False)

def delete_contact():   
    match id.delete_vibor():
        case '1':
            mem = pd.read_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_7/data.csv')
            mem.drop(labels=[int(id.delete_vvod('Индекс'))], axis=0, inplace=True)
            mem.to_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_7/data.csv', index=False)
        case '2':
            mem = pd.read_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_7/data.csv')
            mem = mem.set_index('Фамилия')
            mem.drop([id.delete_vvod('Фамилию')], axis=0, inplace=True)
            mem.to_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_7/data.csv', index=True)

def find_contact():
    mem = pd.read_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_7/data.csv')
    match id.find_vibor():
        case '1':           
            od.vivod_viborka(mem.loc[mem['Фамилия'] == id.find_vvod("Фамилию")])
        case '2':
            od.vivod_viborka(mem.loc[mem['Имя'] == id.find_vvod("Имя")])
        case '3':
            od.vivod_viborka(mem.loc[mem['Телефонный номер'] == id.find_vvod("Телефонный номер")])
        case '4':
            od.vivod_viborka(mem.loc[mem['Комментарий'] == id.find_vvod("Комментарий")])
