class Phone:

    @classmethod
    def show(cls): #<classmethod object at 0x0000011876033390>
        print(f"Running {cls.__name__}")

    def describe(self): #describe': <function Phone.describe at 0x0000011877FC8510>
        print(f"Describing {self}")

print(Phone.__dict__)

Phone.show()
#Phone.describe() <- nie zadziała

phone = Phone()
phone.describe()
phone.show()
print("\n\n ===============Przykład1=============== \n\n")
###Przykład
class Phone:

    instances = []

    def __init__(self):
        Phone.instances.append(self) ##Musimy przez klase dostać się

    @classmethod
    def show(cls):
        if len(Phone.instances) > 0:
            print(f"List of instances of the {Phone.__name__} class:")
            for instanc in Phone.instances:
                print(f"\t{instanc}")
        else:
            print("No instances of the {Phone.__name__} class")

Phone.show()
phone1 = Phone()
phone2 = Phone()
Phone.show()
phone3 = Phone()
phone3.show()
print("\n\n ===============Przykład2=============== \n\n")
###Przykład
class Phone:

    instances = []

    def __init__(self, brand):
        self.brand = brand
        Phone.instances.append(self) ##Musimy przez klase dostać się

    @classmethod
    def show(cls):
        if len(Phone.instances) > 0:
            print(f"List of instances of the {Phone.__name__} class:")
            for instanc in Phone.instances:
                print(f"\t{instanc}")
        else:
            print("No instances of the {Phone.__name__} class")

    def show_brand(self):
        print(f"Brand of Phone:{self.brand}")

phone1 = Phone("Apple")
phone2 = Phone("Samsung")

Phone.show()

for inst in Phone.instances:
    inst.show_brand()


class Worker:
    instances = []

    def __init__(self):
        Worker.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(Worker.instances)


worker1 = Worker()
worker2 = Worker()
worker3 = Worker()

print(worker3.count_instances())