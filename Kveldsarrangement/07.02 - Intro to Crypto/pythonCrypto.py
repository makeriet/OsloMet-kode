Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]

CryptoList = ["!", "?", "+", "1", "<", ".", ",", ">", "2", "#", "3", "%", "(",
 "4", "/", "5", "[", "]", "9", "}", "{", "8", "7", "6", "&", "$"]

secret = "Hello World!"
crypto = ""

for character in secret.upper():
    num = ord(character) - 65
    if num >= 0:
        crypto = crypto + CryptoList[num%26]
    else:
        crypto = crypto + " "

print(crypto)
