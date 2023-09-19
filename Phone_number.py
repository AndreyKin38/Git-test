from random import randint
from string import ascii_lowercase, digits, ascii_uppercase
from collections import deque


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = self.fio = None
        self.__next = None
        self.__prev = None
        if type(number) == int and len(str(number)) == 11 and type(fio) == str:
            self.number = number
            self.fio = fio

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj


class PhoneBook:

    def __init__(self):
        self.first = None
        self.last = None

    def add_phone(self, phone):
        if self.last:
            self.last.next = phone
            phone.prev = self.last
            self.last = phone
        elif self.first:
            self.first.next = phone
            phone.prev = self.first
            self.last = phone
        else:
            self.first = phone

    def remove_phone(self, fio):
        top = self.first
        next = self.first.next

        while top:

            if top.fio != fio:
                top = next
            else:
                if top.fio == self.first.fio:
                    if next:
                        self.first = next
                        self.first.next = None










                return top






book = PhoneBook()

phone1 = PhoneNumber(89621081240, 'Kin Andrey1')
phone2 = PhoneNumber(89621081241, 'Kin Andrey2')
phone3 = PhoneNumber(89621081242, 'Kin Andrey3')
book.add_phone(phone1)
book.add_phone(phone2)
# book.add_phone(phone3)
print(book.__dict__)
# book.remove_phone('Kin Andrey3')

print(book.remove_phone('Kin Andrey1'))
print(book.__dict__)
# print(phone1.prev)
# print(phone2.prev.fio)
# print(phone3.next)
print(book.first.next)