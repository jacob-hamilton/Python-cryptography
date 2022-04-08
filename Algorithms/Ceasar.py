ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def ceasarCipher(plainText, key) -> str: # Key will be an integer.
    return ''.join([ALPHABET[(ALPHABET.index(plainText[i].lower())+key)%len(ALPHABET)] for i in range(0, len(plainText))])

def inverseCeasarCipher(plainText, key) -> str:
    return ''.join([ALPHABET[(ALPHABET.index(plainText[i].lower())-key)%len(ALPHABET)] for i in range(0, len(plainText))])