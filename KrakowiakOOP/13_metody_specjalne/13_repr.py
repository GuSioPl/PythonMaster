##print(help(object.__repr__))
##print(help(repr))
##print(repr(object))

class Phone:

    def __init__(self, brand):
        self.brand = brand

print(Phone)
print(repr(Phone))
print(Phone.__repr__)
phone = Phone("Apple")
print(repr(phone))
print(phone)


class Phone2:

    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"Phone(brand='{self.brand}')"

phone2 = Phone2("Apple")
print(repr(phone2)) ##Mamy formalną reprezentacje naszego obiektu
print(phone2) ##tu tyż
print(eval(repr(phone2))) ##Reprezentacja obiektu powinna pozwolić na jego ponowne utworzenie
phone21 = eval(repr(phone2))##Reprezentacja obiektu powinna pozwolić na jego ponowne utworzenie
print(phone21.brand)
print(eval(repr(phone2)), id(phone2))
print(id(phone21)) ## inny obiekt Inne id