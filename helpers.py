from datetime import datetime
import re

from prettytable import PrettyTable


commands_worlds = ('add', 'add info', 'change', 'close', 'days', 'delete', 'delete note', 'exit', 'find', 'find note', 'find tag', 'good bye', 'hello', 'show', 'show all', 'sort birthday', 'sort name', 'sort note', 'sort surname', 'show field')


commands_int = [i for i in range(len(commands_worlds) + 1)]



class WrongDateFormat(Exception):
    pass


class WrongPhoneNumberFormat(Exception):
    pass


class WrongEmailFormat(Exception):
    pass

class DataNotFound(Exception):
    pass

def check_birthday_date(date):
    BIRTH_REG = re.compile(r"(\d{2})\s(\d{2})\s(\d{4})")

    if BIRTH_REG.match(date):
        return True
    else:
        raise WrongDateFormat


def check_phone_number(number):
    PHONE_REGEX = re.compile(r"^380\d{2}\d{7}$")

    if PHONE_REGEX.match(str(number)):
        return True
    else:
        raise WrongPhoneNumberFormat


def check_valid_email(email):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    if EMAIL_REGEX.match(str(email)):
        return True
    else:
        raise WrongEmailFormat


def find_item(data, item):
    for record in data:
        for key, value in record.items():
            if key == item:
                return record

def find_unit(data, unit, item):
    found_records_list = []
    for record in data:
        for key, value in record.items():
            for i in value[unit]:
                if i.lower().find(item.lower()) != -1:
                    found_records_list.append(record)      

    return found_records_list           

def show_table(data):
    x = PrettyTable()
    list_for_field_names = ['ID', 'Name']
    list_for_row = []

    for key, value in data[0].items():
        for item in value:
            list_for_field_names.append(item.title())
    
    x.field_names = list_for_field_names
    for idx, record in enumerate(data):
        for name, value in record.items():
            list_for_row.append(idx + 1)
            list_for_row.append(name)
            for item in value.values():
                if type(item) == list and len(item) >= 1:
                    list_for_row.append(item[0]) # Добавляем только первый элемент
                elif not item:
                    list_for_row.append('/empty/')
                else:
                    list_for_row.append(item)
            if list_for_row:
                x.add_row(list_for_row)
                list_for_row = []
    return x

def show_record(record):
    x = PrettyTable()
    title = ['Name']
    row = []

    for name, value in record.items():
        row.append(name)
        for key, value in value.items():
            title.append(key.title())
            if type(value) == list and len(value) >= 1:
                row.append(value[0]) # Добавляем только первый элемент
            elif not value:
                list_for_row.append('/empty/')
            else:
                row.append(value)

    x.field_names = title
    x.add_row(row)
    return x

def show_field(data, field):
    x = PrettyTable()
    title = ['ID']
    row = []
    title.append(field)

    if type(data) == list:
        for idx, item in enumerate(data):
            row.append(idx + 1)
            row.append(item)
            x.add_row(row)
            row = []
    else:
        row.append(data)


    print('cont')
    x.field_names = title
    return x

def sort_name(data):
    name_list = []
    if data:
        for record in data:
            for key in record:
                name_list.append(key)
        
        sort_name_list = sorted(name_list)
        sort_list = sorted(data, key=lambda d: [k in d for k in sort_name_list], reverse=True)
        return sort_list
    else:
        return 'Database is empty!'

def sort_surname(data):
    dict_ = []
    sort_dict = []
    if data:
        for record in data:
            for value in record.values():
                dict_.append(value)
        dict_ = sorted(dict_, key=lambda k: k['surname'])

        for item in dict_:
            for record in data:
                for value in record.values():
                    if item == value:
                        sort_dict.append(record)
        
        return sort_dict
    else:
        return 'Database is empty!'

def sort_len_note(data):
    dict_ = []
    sort_dict = []
    if data:
        for record in data:
            for value in record.values():
                dict_.append(value)
        dict_ = sorted(dict_, key=lambda k: len(k['note']), reverse=True)

        for item in dict_:
            for record in data:
                for value in record.values():
                    if item == value:
                        sort_dict.append(record)
            
        return sort_dict
    else:
        return 'Database is empty!'

def sort_birthday(data):
    dict_ = []
    sort_dict = []
    if data:
        for record in data:
            for value in record.values():
                dict_.append(value)
        dict_ = sorted(dict_, key=lambda k: datetime.strptime(k['birthday'], '%d %m %Y'), reverse=True)

        for item in dict_:
            for record in data:
                for value in record.values():
                    if item == value:
                        sort_dict.append(record)
            
        return sort_dict
    else:
        return 'Database is empty!'

def check_double(data, field, value):
    for record in data:
        for item in record.values():
            if str(value) in item[field]:
                return False
    return True

def print_comands():
    print('Available commands:')
    for idx, comand in enumerate(commands_worlds):
        print(idx + 1, '-', comand, sep='-')

def check_data(data, fn):
    if data:
        fn()
    else:
        print('Data not found!')