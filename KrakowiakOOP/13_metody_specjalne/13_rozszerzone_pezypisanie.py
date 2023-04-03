"""
+=	object.__iadd__(self, other)
-=	object.__isub__(self, other)
*=	object.__imul__(self, other)
/=	object.__itruediv__(self, other)
<	object.__lt__(self, other)
<=	object.__le__(self, other)
>	object.__gt__(self, other)
>=	object.__ge__(self, other)
==	object.__eq__(self, other)
!=	object.__ne__(self, other)
"""

class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        if not isinstance(other, Doc):
            return NotImplemented
        return Doc(self.string + ' ' + other.string)

Doc.__dict__

doc1 = Doc('Object')
doc2 = Doc('Oriented')
doc3 = Doc('Programming')

doc1 += doc2

print(doc1) ##działa

class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __iadd__(self, other):
        if not isinstance(other, Doc):
            return NotImplemented
        return Doc(self.string + '-' + other.string)

Doc.__dict__

doc1 = Doc('Object')
doc2 = Doc('Oriented')
doc3 = Doc('Programming')

doc1 += doc2

print(doc1)
print()

class Lengh:

    def __init__(self, lengh):
        self.lengh = lengh

    def __repr__(self):
        return f"Doc(string='{self.lengh}')"

    def __str__(self):
        return f'{self.lengh}'

Lengh.__dict__

l1 = Lengh(4)
l2 = Lengh(3)
l3 = Lengh(4)

print(l1 == l3) ##Dostajemy false bo id się nie zgadzają i z defoultu mamy porównanie ID
l1 = l3

print(l1 == l3) #teraz prawda bo to ten


class Lengh:

    def __init__(self, lengh):
        self.lengh = lengh

    def __repr__(self):
        return f"Doc(string='{self.lengh}')"

    def __str__(self):
        return f'{self.lengh}'

    def __eq__(self, other): ##Sprawdzamy czy długosć jest równa
        if not isinstance(other, Lengh):
            return NotImplemented
        return len(str(self.lengh)) == len(str(other.lengh))

Lengh.__dict__

l1 = Lengh(4455)
l2 = Lengh(36)
l3 = Lengh(4999)

print(l1 == l2, l1 == l3)
##print(l1 < l2) ##nie możemy porównać wywali

class Lengh:

    def __init__(self, lengh):
        self.lengh = lengh

    def __repr__(self):
        return f"Doc(string='{self.lengh}')"

    def __str__(self):
        return f'{self.lengh}'

    def __eq__(self, other): ##Sprawdzamy czy długosć jest równa
        if not isinstance(other, Lengh):
            return NotImplemented
        return len(str(self.lengh)) == len(str(other.lengh))

    def __lt__(self, other): ##Sprawdzamy liczbe pod lengh
        if not isinstance(other, Lengh):
            return NotImplemented
        return self.lengh < other.lengh

    def __le__(self, other): ##Sprawdzamy liczbe pod lengh
        if not isinstance(other, Lengh):
            return NotImplemented
        return self.lengh <= other.lengh

Lengh.__dict__

l1 = Lengh(4455)
l2 = Lengh(36)
l3 = Lengh(4999)

print(l1 < l2, l1 <= l2, l2 < l3) ## już działa
print("\n\n ===== Hash  ======= \n\n")
print(help(hash))
class Lengh:

    def __init__(self, lengh):
        self.lengh = lengh

    def __repr__(self):
        return f"Doc(string='{self.lengh}')"

    def __str__(self):
        return f'{self.lengh}'


l1 = Lengh(4455)
l2 = Lengh(36)

print(hash(l1), hash(l2))


class Lengh:

    def __init__(self, lengh):
        self.lengh = lengh

    def __repr__(self):
        return f"Doc(string='{self.lengh}')"

    def __str__(self):
        return f'{self.lengh}'

    def __eq__(self, other): ##Sprawdzamy czy długosć jest równa
        return isinstance(other, Lengh) and len(str(self.lengh)) == len(str(other.lengh))

l1 = Lengh(4455)
l2 = Lengh(4455)
l3 = Lengh(4999)

#print(hash(l1), hash(l2)) Jeżeli mamy same equal to metoda Hash jest na wartość non ustawiona
#Jeżeli klasa nie definuje metody equal to również nie powinna operacji hash definiowac
#Jeżeli definuje equal a nie definuje hash to instancje nie mogą być używane w elementach hashowanych
#dOMYŚLNIE klasy definiowane będą dziedziczyć bo object te metody więc jak zmieniamy jedno to oba a najlepiej to nie tykać

class Lengh:

    def __init__(self, lengh):
        self.lengh = lengh

    def __repr__(self):
        return f"Lengh(string='{self.lengh}')"

    def __str__(self):
        return f'{self.lengh}'

    def __eq__(self, other): ##Sprawdzamy czy długosć jest równa
        return isinstance(other, Lengh) and len(str(self.lengh)) == len(str(other.lengh))

    def __hash__(self):
        return hash(self.lengh)

l1 = Lengh(4455)
l2 = Lengh(4455)
l3 = Lengh(4999)

print(hash(l1),hash(l2), hash(l3)) ## będzie działać bo zdefiniowaliśmy

class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __eq__(self, other): ##Sprawdzamy czy długosć jest równa
        return isinstance(other, Lengh) and len((self.string)) == len((other.lengh))

    def __hash__(self):
        return hash(self.string)

d1 = Doc("XYZ")
d2 = Doc("XZZ")
d3 = Doc("XYZ")


print(hash(d1),hash(d2), hash(d3))

print("\n\n ===== call  ======= \n\n")

class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __call__(self):
        print(f"Wywolanie {self}")


d1 = Doc("XYZ")
print(d1()) ## bez cala wywaliło