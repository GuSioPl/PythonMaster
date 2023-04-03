def alphanumeric2(password):
    if len(password) == 0:
        return False
    for char in password:
        if not (ord(char) in range(47,58) or ord(char.upper()) in range(65,91)):
            return False
    return True

def alphanumeric(password):
    valid = set('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789')
    if (len(password) ==0 ) or len(set(password).difference(valid)) != 0:
        return False
    return True

def alphanumeric(password):
    valid = set('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789')
    return (False if (len(password) ==0 ) or len(set(password).difference(valid)) != 0 else True)

print(alphanumeric('nariuSz'))
print(alphanumeric(''))
print(alphanumeric('_'))
print(alphanumeric('/PassW0rd'))

for i in range(65,91):
    print(chr(i)," = ", i , end='')
    print(chr(i+32)," = ", i , end='')
print("\n", ord('/'))
for i in range(48,58):
    print(chr(i), end='')

print("\n", ord('/'))
"""
def alphanumeric(password):
    valid = set('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789')
    if (len(password) ==0 ) or len(set(password).difference(valid)) != 0:
        return False
    return True
"""