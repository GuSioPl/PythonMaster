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

print(Doc.__dict__)

doc1 = Doc('Object')
doc2 = Doc('Oriented')
doc3 = Doc('Programming')
#Nie da się dodawać dopuki nie dodamy __add

print(doc3)
print(repr(doc3))
print(repr(doc1 + doc2 + doc3))