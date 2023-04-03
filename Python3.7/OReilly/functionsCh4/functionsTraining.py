import modules.someFunctions


def properDiffrenceFunction(a:int, b:int=0) ->int:
    """This function purpose is to add two integer numbers"""
    return a - b

print(properDiffrenceFunction(3,1))
print(properDiffrenceFunction(b=1,a=3))
print(properDiffrenceFunction(3))
help(properDiffrenceFunction)
print(modules.someFunctions.simpleAddition(3,4))
help(modules.someFunctions.simpleAddition)

def double(arg): #By argument (no changing value of argument)
    print("Before -",arg)
    arg = arg *2
    print("After -", arg)

def change(arg): #By reference data changed /by addres argument?
    print("Before -",arg)
    arg.append('More data')
    print("After -", arg)

a = 10
b = ['Data and']
print(a,b)
double(a)
change(b)
print(a,b)