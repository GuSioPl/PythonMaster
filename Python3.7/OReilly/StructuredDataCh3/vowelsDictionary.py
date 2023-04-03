def dictionaryVowelFromBook(word):
    vowels = ['a','i','e','o','u']
    found = {}
    found['a'] = 0
    found['i'] = 0
    found['e'] = 0
    found['o'] = 0
    found['u'] = 0
    for letter in word:
        if letter in vowels:
            found[letter] += 1
    for k, v in sorted(found.items()):
        print(k, 'was found', v, 'time(s).')


def dictionaryMyTry(word):
    vowels = ['a','i','e','o','u']
    word = [letter for letter in word if letter in vowels]
    found = {vowel: word.count(vowel) for vowel in vowels}
    for k, v in sorted(found.items()):
        print(k, 'was found', v, 'time(s).')

def dictionaryMyTry2(word):
    vowels = ['a','i','e','o','u']
    found = {}
    for letter in word:
        if letter in vowels:
            if letter not in found: found.setdefault(letter,0)
            found[letter] += 1
    for k, v in sorted(found.items()):
        print(k, 'was found', v, 'time(s).')

dictionaryMyTry2("Mariuuuussszyyyii")
##for i in vowels: print("found['{}'] = 0 \n".format(i),end="") <<--Faster then manualy writing found.....