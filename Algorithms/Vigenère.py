alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def vigenereCipher(plainText, key):
    key = paddKey(plainText, key.lower())
    plainText = plainText.lower()
    result = ""
    for i in range(0, len(plainText)):
        result += vignereTable(plainText[i], key[i])
    return result

def inverseVigenereCipher(cipherText, key):
    key = paddKey(cipherText, key.lower())
    result = ""
    for i in range(0, len(cipherText)):
        result += inverseVignereTable(key[i], cipherText[i])
    return result

def vignereTable(rowLetter, columnLetter):
    temp = alphabet
    for i in range(alphabet.index(rowLetter)):
        temp.append(temp[0])
        temp = temp[1:]
    return temp[alphabet.index(columnLetter)]

def inverseVignereTable(keyLetter, cipherLetter):
    temp = alphabet
    for i in range(alphabet.index(keyLetter)):
        temp.append(temp[0])
        temp = temp[1:]
    return alphabet[temp.index(cipherLetter)]

def paddKey(plainText, key):
    plainTextLength = len(plainText)
    count = 0

    if len(key) < plainTextLength:
        while len(key) < plainTextLength:
            key += key[count]
            count += 1
        return key

    if len(key) > plainTextLength:
        return key[0:plainTextLength]
    
    return key