from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode())

def decrypt(token, key):
    f = Fernet(key)
    return f.decrypt(token).decode()
