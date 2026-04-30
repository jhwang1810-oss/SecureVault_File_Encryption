from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES

def derive_key(password, salt):
    return PBKDF2(password, salt, kdLen = 32)

def encrypt(message, password):
    message = message.encode()

    salt = get_random_bytes(16)
    key = derive_key(password, salt)

    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message)

    return salt, cipher.nonce, tag, ciphertext

def decrypt(password, salt, nonce, tag, ciphertext):
    key = PBKDF2(password, salt, dkLen = 32)
    cipher = AES.new(key, AES.MODE_GCM, nonce = nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext.decode()



     

