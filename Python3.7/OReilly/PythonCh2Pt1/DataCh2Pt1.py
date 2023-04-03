import random
randNumber = random.randint(1,60)

print(randNumber)

vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U']

word = input("Please enter word \n")

print(word, ' have only this')
lettersInWord = []
for letter in word:
    if letter in vowels:
        lettersInWord.append(letter)
        print(letter, end='')

print(" ", len(lettersInWord), "vowels")
print("\nAnd non-volwers in ", word, " are: ",end='')
for letter in word:
    if letter not in vowels:
        lettersInWord.extend(letter)
        print(letter, end='')

print(lettersInWord)