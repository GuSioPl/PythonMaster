####1########
import sys
print(sys.version.split(' ')[0])

import datetime


print(sorted(datetime.__dict__))

import uuid


class Product:

    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

for name in Product.__dict__.keys():
    print(name)


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} -> {self.age}'


people = [Person('Tom', 25), Person('John', 29),
          Person('Mike', 27), Person('Alice', 19)]

for person in sorted(people, key=lambda student: student.age):
    print(person)

def stock_info(company, country, price, currency):
    return f'Company: {company}\nCountry: {country}\nPrice: {currency} {price}'

print(stock_info.__code__.co_varnames)
########################


import builtins

print(help(builtins.sum))

print(sum([-4, 3, 2]))

######

counter = 1

def update_counter():
    global counter
    counter += 1
    print(counter)

counter = 0
dot_counter = ''

def update_counter():
    global counter, dot_counter
    counter += 1
    dot_counter += '.'

for i in range(40):
    update_counter()

print(counter,'\n',dot_counter)


def display_info(number_of_updates=1):
    counter = 100
    dot_counter = ''

    def update_counter():
        nonlocal counter
        nonlocal dot_counter
        counter += 1
        dot_counter += '.'

    [update_counter() for _ in range(number_of_updates)]

    print(counter)
    print(dot_counter)

display_info(10)