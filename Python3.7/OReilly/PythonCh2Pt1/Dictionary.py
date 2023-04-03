vowels = ['a', 'e', 'o', 'i', 'u']
word = input("Please provide word")
found = {'a':0, 'e':0, 'o':0, 'i':0, 'u':0}
for letter in word:
    if letter in found:
        found[letter] += 1
print(found)
