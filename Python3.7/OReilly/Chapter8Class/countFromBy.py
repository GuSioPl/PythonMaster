class CountFromBy:
    def __init__(self, v:int=0, i:int=1) -> None:
        self.val = v
        self.incr = i

    def __repr__(self) -> str:
        return str(self.val)


    def increase(self)->None:
        self.val += self.incr

a = CountFromBy()
a.increase()
print(a)
print(type(a))
print(id(a))
print(hex(id(a)))
print(a.incr)
# CountFromBy.increase(c) = c.increase()
