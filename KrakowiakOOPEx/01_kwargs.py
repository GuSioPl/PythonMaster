




def display_info(company, **kwargs):
    print(f"Company name: {company}")
    for kwar in kwargs.items():
        if str(kwar[0]) == 'price':
            print(f"{kwar[0].title()}: $ {kwar[1]}")
        else:
            print(f"{kwar[0].title()}: {kwar[1]}")

display_info("Krzysiek",price = 30, price2 = 80)

class Phone:
    pass

print(type(Phone))


class Phone:
    brand = 'Apple'
    model = 'iPhone X'


print(getattr(Phone, 'brand'))
print(getattr(Phone, 'model'))


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


OnlineShop.country = 'Poland'

print(OnlineShop.__dict__.keys())
print(OnlineShop.__dict__.keys())
print([atr for atr in OnlineShop.__dict__.keys() if not str(atr)[:2] == '__' ])
print([atr for atr in OnlineShop.__dict__.keys() if not atr.startswith('__')])


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False

    def __repr__(self):
        print(f'sector -> {self.sector}')
        print(f'sector_code  -> {self.sector_code}')
        print(f'is_public_company  -> {self.is_public_company}')

shop = OnlineShop()

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False



print(f'sector -> {OnlineShop.sector}')
print(f'sector_code -> {OnlineShop.sector_code}')
print(f'is_public_company -> {OnlineShop.is_public_company}')

class Book:
    language = 'ENG'
    is_ebook = True


book_1 = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

books = [book_1, book_2]

for book in books:
    for key, value in book.__dict__.items():
        print(key, '->', value)
    print('------------------------------')

for book in books:
    for attr in book.__dict__:
        print(f'{attr} -> {getattr(book, attr)}')
    print('-' * 30)


class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_attrs_with_values(self):
        for key, value in self.__dict__.items():
            print(f"{key} -> {value}")


laptop = Laptop('Dell', 'Inspiron', 3699)

laptop.display_attrs_with_values()




class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price

    def display_info(self):
        for key,value in self.__dict__.items():
            if str(key).startswith('_'):
                key = str(key).split('_')[-1]
            print(f'{key} -> {value}')



laptop = Laptop('Acer', 'Predator', 5490)
laptop.display_info()


class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_private_attrs(self):
        for key, item in self.__dict__.items():
            if str(key).startswith(f'_{self.__class__.__name__}'):
                print(f'{key}')


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_private_attrs()

class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_protected_attrs(self):
        for key, item in self.__dict__.items():
            if str(key).startswith(f'_') and not str(key).startswith(f'_{self.__class__.__name__}'):
                print(f'{key}')


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_protected_attrs()


class Laptop:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if value <= 0 or not isinstance(value, (float, int)):
            raise TypeError('The price attribute must be an int or float type.')
        self._price = value


laptop = Laptop(3499)
try:
    laptop.set_price(-3000)
except ValueError as error:
    print(error)