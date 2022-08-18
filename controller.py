import input_data as id
import output_data as od
import func
import pandas as pd

def start():
    match id.vibor():
        case '1': 
            func.create_new_book()
        case '2':
            func.add_number(pd.read_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_7/data.csv'))
        case '3':
            func.delete_contact()
        case '4':
            od.vivod_file()
        case '5':
            func.find_contact()

