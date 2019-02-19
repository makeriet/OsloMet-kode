Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]

secret = "Hello World"
crypto = ""

for character in secret.upper():
    num = ord(character) - 65
    if num >= 0:
        crypto = crypto + Alphabet[(num + 2)%26]
    else:
        crypto = crypto + " "

print(crypto)
