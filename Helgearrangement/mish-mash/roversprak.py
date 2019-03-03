consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

string = input("Skriv setning: ")

newString = ""

for letter in string:
    if letter.lower() in consonants:
        newString += letter + "o" + letter.lower()
    else:
        newString += letter

print(newString)
