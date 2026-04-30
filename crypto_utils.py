# crypto_utils.py

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES


def derive_key(password, salt):
    return PBKDF2(password.encode(), salt, dkLen=32)


# 🔐 FILE ENCRYPTION
def encrypt_file(filename, password):
    with open(filename, "rb") as f:
        data = f.read()

    salt = get_random_bytes(16)
    key = derive_key(password, salt)

    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    output_file = filename + ".bin"

    with open(output_file, "wb") as f:
        f.write(salt)
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

    print(f"Encrypted file saved as {output_file}")


# 🔓 FILE DECRYPTION
import os

def decrypt_file(filename, password):
    with open(filename, "rb") as f:
        salt = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    # ✅ FIXED OUTPUT PATH
    base = os.path.basename(filename)              # Passwords.pages.bin
    name = base.replace(".bin", "")                # Passwords.pages
    output_file = os.path.join(
        os.path.dirname(filename),
        "decrypted_" + name
    )

    with open(output_file, "wb") as f:
        f.write(plaintext)

    print(f"Decrypted file saved as {output_file}")