# storage.py

def save_encrypted(filename, salt, nonce, tag, ciphertext):
    """
    Save encrypted data to a file in binary format.
    Format:
    [salt (16)] [nonce (16)] [tag (16)] [ciphertext]
    """
    with open(filename, "wb") as f:
        f.write(salt)
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)


def load_encrypted(filename):
    """
    Load encrypted data from file and return components.
    Must match the exact order used in save_encrypted.
    """
    with open(filename, "rb") as f:
        salt = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    return salt, nonce, tag, ciphertext