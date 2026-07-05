def encrypt(text, keyword):
    text1 = ""
    key_i = 0
    keyword = keyword.upper()
    for i in range(len(text)):
        ch = text[i]
        if text[i].isalpha():
            shift = ord(keyword[key_i % len(keyword)]) - ord('A')
            if text[i].isupper():
                ch = chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
            elif text[i].islower():
                ch = chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a'))
            key_i += 1
        text1 += ch
    return text1

def decrypt(text, keyword):
    text1 = ""
    key_i = 0
    keyword = keyword.upper()
    for i in range(len(text)):
        ch = text[i]
        if text[i].isalpha():
            shift = ord(keyword[key_i % len(keyword)]) - ord('A')
            if text[i].isupper():
                ch = chr((ord(text[i]) - ord('A') - shift) % 26 + ord('A'))
            elif text[i].islower():
                ch = chr((ord(text[i]) - ord('a') - shift) % 26 + ord('a'))
            key_i += 1
        text1 += ch
    return text1
