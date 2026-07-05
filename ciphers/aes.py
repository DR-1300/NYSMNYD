from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_a(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode()).decode() 

def decrypt_a(token, key):
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()
