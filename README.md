# NYSMNYD 🔐
### *Now You See Me, Now You Don't*
 
> An encryption/decryption CLI tool built in Python — supporting Caesar, Vigenère, and AES encryption for both text and files.
 
---
 
## What does the name mean tho 😭

The name origin is actually some weird corelation that i thought would work ( like you see something once, but after you encypt it, u cant see it because it has changed )

---
 
## How it works
 
NYSMNYD supports three encryption methods, each progressively stronger than the last:
 
### Caesar Cipher
Julius Caesar used this for his personal correspondence. Each letter of the text is shifted to the right by some number to give it a different letter. 
 
```
"Hello" with shift 3 → "Khoor"
```
 
Mathematically:
- Encrypt: `E(x) = (x + n) mod 26`
- Decrypt: `D(x) = (x - n) mod 26`
Simple, but crackable via frequency analysis — the letter `E` just becomes another letter, and patterns survive.
 
---
 
### Vigenère Cipher
Vigenere is basically Caesar cipher but instead of one fixed shift, you use a keyword where each letter of the keyword gives a different shift. The keyword repeats to match the length of the text.
 
```
"HELLO" with keyword "KEY" → "RIJVS"
K=10, E=4, Y=24, K=10, E=4
```
 
Stronger than Caesar because frequency analysis no longer works directly — each letter can map to multiple encrypted letters.
 
---
 
### AES (Advanced Encryption Standard)
Selected by the US government (NIST) in 2001 after a 5-year global competition where cryptographers worldwide submitted algorithms and tried to break each other's. AES won. It's now the global standard — used in WhatsApp, HTTPS, and banking.
 
Unlike Caesar and Vigenère, AES doesn't encrypt letter by letter. It converts your entire text to raw bytes, then runs them through 10+ rounds of:
- Scrambling positions
- Substituting values via a lookup table
- Mixing columns mathematically
- XORing with the key
The result is **zero patterns** — changing one character in the input completely changes the entire output (the avalanche effect). Without the key, it's mathematically impossible to crack.
 
---
 
## Usage
 
### Text encryption
```bash
python cli.py encrypt --method caesar --shift 3 --text "Hello World"
python cli.py decrypt --method caesar --shift 3 --text "Khoor Zruog"
 
python cli.py encrypt --method vigenere --keyword KEY --text "Hello World"
python cli.py decrypt --method vigenere --keyword KEY --text "Rijvs Uyvjn"
 
python cli.py encrypt --method aes --text "Hello World"
python cli.py decrypt --method aes --text "<encrypted_output>"
```
 
### File encryption
```bash
python cli.py encrypt --method aes --file secret.txt
# creates secret.txt.encrypted
 
python cli.py decrypt --method aes --file secret.txt.encrypted
# creates secret.txt.encrypted.decrypted
```
 
> **Note:** AES automatically saves the key to `secret.key` on encrypt and reads it back on decrypt. Keep this file safe — without it, decryption is impossible.
 
---
 
## Tech stack
- Python 3
- `argparse` -  CLI interface
- `cryptography` - AES via Fernet
---