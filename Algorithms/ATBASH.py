CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def atbash(plainText):
    return ''.join([CHARACTERS[len(CHARACTERS)-1-CHARACTERS.index(plainText[i])] for i in range(0, len(plainText))])

def inverseAtbash(cipherText):
    return ''.join([CHARACTERS[len(CHARACTERS)-1-CHARACTERS.index(cipherText[i])] for i in range(0, len(cipherText))])

# Atbash is a very weak algorithm. All it does is reverse the alphabet.