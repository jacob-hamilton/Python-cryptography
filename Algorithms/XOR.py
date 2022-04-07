def stringXOR(plainText, key, returnAsBinary=False): # Main file to XOR a string and a key.
    key = paddKey(plainText, key)
    plainTextBinary, keyBinary = convertToBinary(plainText), convertToBinary(key)
    result = ""
    for i in range(0, len(plainTextBinary)):
        if plainTextBinary[i] == '1' and keyBinary[i] == '1':
            result += '0'
        elif plainTextBinary[i] == '0' and keyBinary[i] == '0':
            result += '0'
        else:
            result += '1'
    
    if returnAsBinary:
        return result
    
    else:
        return convertToString(result)
    

def paddKey(plainText, key):
    plainTextLength, keyLength = len(plainText), len(key)
    if plainTextLength > keyLength:
        key = addKeyLength(plainTextLength, key)
    elif plainTextLength < keyLength:
        key = key[0:plainTextLength]
    
    return key

def addKeyLength(plainTextLength, key):
    count = 0
    while len(key) < plainTextLength:
        key += key[count]
        count += 1

    return key

def paddBinaryNumber(binaryNumber):
    while len(binaryNumber) < 8:
        binaryNumber = "0"+binaryNumber
    return binaryNumber

def convertToBinary(inputString):
    binaryString = ""
    for i in range(0, len(inputString)):
        binaryString += paddBinaryNumber(bin(ord(inputString[i]))[2:])
    return binaryString

def convertToString(inputBinaryString):
    parts = [inputBinaryString[i:i+8] for i in range(0, len(inputBinaryString), 8)]
    result = ""
    for count, part in enumerate(parts):
        result += chr(int(part, 2))
    return result
