class Integer:

    def __init__(self, number=0):
        self.number = int(number)

    def __str__(self):
        return f'{self.number}'

    def __repr__(self):
        return f"Integer(number='{self.number}')"

    def __add__(self, other):
        if not isinstance(other, Integer):
            return NotImplemented
        return self.number + other.number

    def __sub__(self, other):
        if not isinstance(other, Integer):
            return NotImplemented
        return self.number - other.number

int1 = Integer()
int2 = Integer(4)
print(int1)
print(int1.__repr__())
print(int1 - int2)


class Worker:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Worker=(fname='{self.fname}', lname='{self.lname}')"


worker = Worker('John', 'Doe')
print(worker)
