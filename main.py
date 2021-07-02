from collections import UserDict
from conn_to_db import create_new_record, FindDataInDb
from datetime import datetime, timedelta
import json

from abc import abstractmethod, ABCMeta

try:
    from helpers import *
except ModuleNotFoundError:
    from .helpers import  *


path = 'data.json'


class Record:
    def __init__(self, name, surname, adress, note, tag, email, phone, birthday):
        self.name = name.value
        self.surname = surname.value
        self.adress = adress.value
        self.note = note.value[0]
        self.tag = tag.value[0]
        self.email = email.value[0]
        self.phone = phone.value[0]
        self.birthday = birthday.value



class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Surname(Field):
    pass


class Adress(Field):
    pass


class Note(Field):
    def __init__(self, note):
        list_note = note.split('.')
        self.__value = []
        self.value = list_note

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, list_note):
        for item in list_note:
            self.__value.append(item.strip())


class Tag(Field):
    def __init__(self, tag):
        list_tag = tag.split(',')
        self.__value = []
        self.value = list_tag

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, list_tag):
        for item in list_tag:
            self.__value.append(item.strip())


class Email(Field):
    flag = True
    def __init__(self, email):
        list_email = email.split(',')
        self.__value = []
        self.value = list_email

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, list_email):
        for item in list_email:
            try:    
                check_valid_email(item.strip())
                self.__value.append(item.strip())
            except WrongEmailFormat: 
                self.flag = False
                print(f'Email "{item}" not valid!')


class Phone(Field):
    flag = True
    def __init__(self, numbers):
        list_numbers = str(numbers).split(',')
        self.__value = []
        self.value = list_numbers

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, list_numbers):

        for item in list_numbers:
            try:
                check_phone_number(item.strip())
                if item not in self.__value:
                    self.__value.append(item.strip())
            except WrongPhoneNumberFormat:
                self.flag = False
                print(f'Number {item} is not valid! Please, enter number in format 380_________')


    def __str__(self):
        return f'Phone: {self.__value}'


class Birthday(Field):
    flag = True
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __getitem__(self, key=None):
        return self.__value

    def __setitem__(self, key, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, data):
        try:
            check_birthday_date(data)
            self.__value = data
        except WrongDateFormat:
            self.flag = False
            print('Please, input birthday date in format "%d %m %Y" ')


classes = {
    'name': Name,
    'surname': Surname,
    'adress': Adress,
    'note': Note,
    'tag': Tag,
    'email': Email,
    'phone': Phone,
    'birthday': Birthday,
}


class AddressBook(UserDict):

    def add_info(self, name):
        data = self.get_data(self)
        if data:
            record = find_item(data, name)
            if record:
                field = input("Enter field: ")
                i = input("Enter new record: ")
                signature_cls = classes[field]
                check_value = signature_cls(i)
                value = check_value.value
                if value:
                    if type(record[name][field]) == list:
                        record[name][field].extend(value)
                        print(f'Note in record {record} changed successfully!')
                        self.save_data(self, data)
                    elif type(record[name][field]) == str:
                        record[name][field] += ',' + ' ' + value
                        print(f'Note in record {record} changed successfully!')
                        self.save_data(self, data)

            else:
                print('Name not found! Please, try again!')
        else:
            print('Database is empty!')

    def add_record(self, record):
        new_record = {record.name: {
            'surname': record.surname,
            'adress': record.adress,
            'note': record.note,
            'tag': record.tag,
            'email': record.email,
            'phone': record.phone,
            'birthday': record.birthday
        }}

        if self.get_data(self):
            current_data = self.get_data(self)
            current_data.append(new_record)
            with open(path, 'w', encoding='utf8') as file:
                json.dump(current_data, file, ensure_ascii=False)
        else:
            # First save
            with open(path, 'w', encoding='utf8') as file:
                json.dump([new_record], file, ensure_ascii=False)
        
        print(f'Record {new_record} added successfully!')

    def get_data(self):
        try:
            with open(path, 'r', encoding='utf8') as file:
                current_data = json.load(file)
            return current_data
        except FileNotFoundError:
            return None

    def save_data(self, data):
        with open(path, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)




def main():

    while True:
        action = input('Choose action: ')

        if action not in commands_worlds and action not in str(commands_int):
            print('Wrong action. Try again!')

        if action == 'add record' or action == str(1):

            name = input("Name:   ")
            name = Name(name)

            surname = input("Surname:   ")
            surname = Surname(surname)

            adress = input("Adress:   ")
            adress_cls = Adress(adress)

            note = input("Note/s:   ")
            note = Note(note)

            tag = input("Tag/s:   ")
            tag = Tag(tag)

            while True:
                birthday = input("Birthday:  ")
                birthday_cls = Birthday(birthday)
                if birthday_cls.flag:
                    break
                
            while True:
                email = input("Email:   ")  
                email_cls = Email(email)
                if email_cls.flag:
                    data = AddressBook.get_data(AddressBook)
                    if data:
                        if check_double(data, 'email', email):
                            break
                        else:
                            print(f'Email {email} used already!')
                    else:
                        break

            while True:
                phone = input("Phone format 380......... :   ")
                phone_cls = Phone(phone)
                if phone_cls.flag:
                    data = AddressBook.get_data(AddressBook)
                    if data:
                        if check_double(data, 'phone', phone):
                            break
                        else:
                            print(f'Phone {phone} used already!')
                    else:
                        break

            record = Record(name, surname, adress_cls, note, tag, email_cls, phone_cls, birthday_cls)
            create_new_record(record)


        elif action == 'change' or action == str(3):
            query = input('Enter query for find. Example: name, surname, adress, email, phone:   '  )            
            name = input(f'Enter the {query} do you want to find:   ')
            field = input(f'Enter the field do you want to update:   ')
            new_data = input(f'Enter the data do you want to update:   ')
            FindDataInDb.update_record(FindDataInDb, query, name, field, new_data)

        elif action == 'show all' or action == str(6):
            FindDataInDb.show_all_records(FindDataInDb)

        elif action == 'delete' or action == str(4):
            query = input('Enter query for find record. Example: id, name, surname, adress, email, phone:   '  )               
            name = input(f'Enter the {query} do you want to delete:   ')
            FindDataInDb.delete_record(FindDataInDb, query, name)

        elif action == 'find' or action == str(2):
            query = input('Enter query for find. Example: name, surname, adress, email, phone:   '  )            
            name = input(f'Enter the {query} do you want to find:   ')
            FindDataInDb.show_records_for_query(FindDataInDb, query, name)


        elif action == 'good bye' or action == 'close' or action == 'exit' or action == str(5):
            print('Bye!')
            break

        elif action == 'help' or action == str(0):
            print_comands()


if __name__ == "__main__":
    print('To see the list of commands, please enter the command help or 0')
    main()

