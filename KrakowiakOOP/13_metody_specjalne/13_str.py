print(object.__str__)
#print(help(str))

class Phone:

    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"Phone(brand='{self.brand}')"

    def __str__(self):
        return f"{self.brand} brand ,mobile phone."

phone = Phone("Apple")
phone #dało by na formalną reprezentacje naszego obiektu jak repr Phone(brand='Apple')
print(phone) #Tutaj nieformalna print(str(phone)) == phone.__str__()
print(repr(phone)) # == phone.__repr__
#jak przekazujemy te funkcje podspodem są wykonywane te mteody __str__ __repr__
print("\n=============BEZ repr===============\n")
class Phone: ## bez repr

    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"{self.brand} brand ,mobile phone."

phone = Phone("Apple")
print(phone.__repr__())
print(phone) ##