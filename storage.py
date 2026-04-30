def save_encrypted(filename, salt, nonce, tag, ciphertext):

    with open(filename, "wb") as f:
        f.write(salt)
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)

def load_encrypted(filename):

    with open(filename, "rb") as f:
        salt = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    return salt, nonce, tag, ciphertext


