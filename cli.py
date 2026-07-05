import argparse
from ciphers.caesar import encrypt_c, decrypt_c
from ciphers.aes import encrypt_a, decrypt_a, generate_key
from ciphers.vigenere import encrypt_v, decrypt_v

parser = argparse.ArgumentParser(description="NYSMNYD encryption tool")
parser.add_argument("action", choices = ["encrypt", "decrypt"])
parser.add_argument("--method", choices = ["caesar", "vigenere", "aes"])
parser.add_argument("--text", help="text to encrypt")
parser.add_argument("--shift", type=int, help="shift for caesar")
parser.add_argument("--keyword", help="keyword for vigenere")
parser.add_argument("--file", help="file to encrypt/decrypt")
args = parser.parse_args()
if args.file:
    with open(args.file, "r") as f:
        contents = f.read()
    if args.action == "encrypt":
        if args.method == "caesar":
            if args.shift is None:
                print("error: casear requires --shift")
                exit()
            else: 
                result = encrypt_c(contents, args.shift)
        elif args.method == "vigenere":
            if args.keyword is None:
                print("error: vigenere requires --keyword")
                exit()
            else:
                result = encrypt_v(contents, args.keyword)
        elif args.method == "aes":
            key = generate_key()
            with open("secret.key", "wb") as f:
                f.write(key)
            result = encrypt_a(contents, key)
        with open(args.file + ".encrypted", "w") as f:
            f.write(result)
    elif args.action == "decrypt":
        if args.method == "caesar":
            if args.shift is None:
                print("error: caesar requires --shift")
                exit()
            else:
                result = decrypt_c(contents, args.shift)
        elif args.method == "vigenere":
            if args.keyword is None:
                print("error: vigenere requires --keyword")
                exit()
            else:
                result = decrypt_v(contents, args.keyword)
        elif args.method == "aes":
            with open("secret.key", "rb") as f:
                key = f.read()
            result = decrypt_a(contents, key)
        with open(args.file + ".decrypted", "w") as f:
            f.write(result)
    

else:
    if args.action == "encrypt":
        if args.method == "caesar":
            if args.shift is None:
                print("error: casear requires --shift")
                exit()
            else: 
                print(encrypt_c(args.text, args.shift))
        elif args.method == "vigenere":
            if args.keyword is None:
                print("error: vigenere requires --keyword")
                exit()
            else:
                print(encrypt_v(args.text, args.keyword))
        elif args.method == "aes":
            key = generate_key()
            with open("secret.key", "wb") as f:
                f.write(key)
            print(encrypt_a(args.text, key))
    elif args.action == "decrypt":
        if args.method == "caesar":
            if args.shift is None:
                print("error: caesar requires --shift")
                exit()
            else:
                print(decrypt_c(args.text, args.shift))
        elif args.method == "vigenere":
            if args.keyword is None:
                print("error: vigenere requires --keyword")
                exit()
            else:
                print(decrypt_v(args.text, args.keyword))
        elif args.method == "aes":
            with open("secret.key", "rb") as f:
                key = f.read()
            print(decrypt_a(args.text, key))