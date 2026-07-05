def encrypt(text, shift):
    text1 = ""
    for i in text:
        ch = i
        if i.isalpha():
            if i.isupper():
                ch = chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
            elif i.islower():
                ch = chr((ord(i) - ord('a') + shift) % 26 + ord('a'))
        text1 += ch
    return text1

def decrypt(text, shift):
    text1 = ""
    for i in text:
        ch = i
        if i.isalpha():
            if i.isupper():
                ch = chr((ord(i) - ord('A') - shift) % 26 + ord('A'))
            elif i.islower():
                ch = chr((ord(i) - ord('a') - shift) % 26 + ord('a'))
        text1 += ch
    return text1