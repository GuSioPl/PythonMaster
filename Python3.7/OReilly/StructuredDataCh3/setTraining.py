vowelsSet= set('aeeeeuuuiiiiioooooyyyyyyyyaaaee')
print(vowelsSet)
lettersRng = "ajfbghkvjbehfoafhslvslkejfsdjhvlakejshw;lfdisdkh;egsdlgfadfs"
print(vowelsSet.union(lettersRng))

def vowels7(found):
    vowelsSet = set('aeoiyu')
    print(set(found).intersection(vowelsSet))

vowels7(lettersRng)

