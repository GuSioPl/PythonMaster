class Phone:

    def show():
        print("Running")

print(Phone.__dict__)
Phone.show()
phone = Phone()
##phone.show() <- wysypie się bo wstrzykuje obiekt phone a ma zero argumentów
print(phone.show)
print("============")
class Phone2:

    def show(self):
        print(f"Running - {self}")

print(Phone2.__dict__)
##Phone2.show() tera to by sie wysypało bo nie podajemy argumentu
phone2 = Phone2()
phone2.show()
#print(help(classmethod))
print("============")

class Phone3:

    def show(cls):
        print(f"Running - {cls.__name__}")

    show = classmethod(show) ##i teraz mamy metode związaną nie z konkretnym obiektem a z naszą klasą

print(Phone3.__dict__) #'show': <classmethod object at 0x00000288363CAE80>
Phone3.show()
phone3 = Phone3()
phone3.show() #nie wywali się już
print("Dla porównaia")
print(phone3.show)
print(phone.show)
print("============")
class Phone4: ## Uproszczenie

    @classmethod
    def show(cls):
        print(f"Running 4 - {cls.__name__}")

Phone4.show()
phone4 = Phone3()
phone4.show()