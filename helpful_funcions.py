import hashlib


def encript(str):
    return hashlib.sha256(str.encode()).hexdigest()
