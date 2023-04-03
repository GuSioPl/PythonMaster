#Metoda statyczna to nie jest związana z klasą ani z instancją klasy działają jak zwykle funkcje
import time

class Phone:

    def get_current_time():
        print(time.strftime("%H:%M:%S", time.localtime()))
        return time.strftime("%H:%M:%S", time.localtime())

print(Phone.__dict__)

Phone.get_current_time() #działa

phone1 = Phone()
## phone1.get_current_time() <<bez static method wywali się bo wstrzykujemy instancje phone1 od klasy Phone

class Phone2:

    def get_current_time(): #<staticmethod object at 0x0000026136187198>
        print(time.strftime("%H:%M:%S", time.localtime()))
        return time.strftime("%H:%M:%S", time.localtime())

    get_current_time = staticmethod(get_current_time)

print(Phone2.__dict__)

phone2 = Phone2()
Phone2.get_current_time()
phone2.get_current_time() ## bANGLA
class Phone2:

    @staticmethod
    def get_current_time(): #<staticmethod object at 0x0000026136187198>
        print(time.strftime("%H:%M:%S", time.localtime()))
        return time.strftime("%H:%M:%S", time.localtime())

print(Phone2.__dict__)

phone2 = Phone2()
Phone2.get_current_time()
phone2.get_current_time() ## bANGLA

print("\n ===============Przykład=============== \n")
class Phone3:

    instances = []

    def __init__(self):
        self.creation_time = Phone3.get_current_time()
        Phone3.instances.append((self))

    @staticmethod
    def get_current_time():
        return time.strftime("%H:%M:%S", time.localtime())

phone31 = Phone3()
time.sleep(1)
phone32 = Phone3()
time.sleep(2)
phone33 = Phone3()
time.sleep(0.3)

for inst in Phone3.instances:
    print(inst.creation_time, inst)

print("\n ===============Przykład 2=============== \n")

class Person:

    def __init__(self, full_name):
        items = full_name.split(' ')
        if len(items) > 1:
            self._name = items[0]
            self._surname = items[1]
        else:
            raise ValueError("The object cannot be created")

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

print(Person.__dict__)

person = Person("Mariusz Pudzianowski")
print(f"Name : {person.name}\nSurname : {person.surname}")
print(f"Name : {person._name}\nSurname : {person._surname}")
#person2 = Person("Pudzian") #- nie zadziała

class Person2:

    def __init__(self, full_name):
        if Person._is_string_with_space(full_name):
            items = full_name.split(' ')
            if len(items) == 2:
                self._name = items[0]
                self._surname = items[1]
            else:
                raise ValueError("The object cannot be created")
        else:
            raise ValueError("Please insert space between name and"
                             " surname or no string provided")

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @staticmethod
    def _is_string_with_space(input_str):
        return isinstance(input_str,str) and ' ' in input_str

print(Person2.__dict__)
person2 = Person2("Mariusz Pudzian")
print(person2.name,person2.surname)