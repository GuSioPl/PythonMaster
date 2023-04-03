def search4vowels(phrase:str) -> set:
    """Function for given string returns set of vowels in it"""
    vowels = set('aeiouyAEIOUY')
    return vowels.intersection(set(phrase))

print(search4vowels(str('Mariuszyyyee')))

def search4letters(phrase:str,letters:str='aieyouAIEOUY') ->set:
    """Function for given string returns set of letters in it"""
    return set(phrase).intersection(set(letters))

print(search4letters("Mariusz","arc"))
print(search4letters("arc"))
