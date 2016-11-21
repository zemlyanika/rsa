from tools import *


def encrypt(message, n, e):
    encrypted = []
    for i in message:
        c = (i**e) % n
        encrypted.append(c)
    return encrypted


def decrypt(encoded_message, n, d):
    decoded = []
    for i in encoded_message:
        m = (i ** d) % n
        decoded.append(m)
    return decoded


def main():
    message = [11, 12, 54, 124, 256, 11]
    n, e, d = generate_keys()
    print(n, e, d)
    encoded = encrypt(message, n, e)
    print("message", message)
    print("encoded", encoded)
    decoded = decrypt(encoded, n, d)
    print("decoded", decoded)
    return

if __name__ == '__main__':
    main()
