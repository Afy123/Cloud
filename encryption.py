from cryptography.fernet import Fernet


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# write_key()


def load_key():
    return open("key.key", "rb").read()


def encrypt_message(message):
    key = load_key()
    encoded_msg = message.encode()
    f = Fernet(key)
    encrypt_msg = f.encrypt(encoded_msg)
    # print(encrypt_msg)
    decrypt_msg = f.decrypt((encrypt_msg))
    # print(decrypt_msg)


# encrypt_message("Hi i am afthab")


def encrypt_file():
    key = load_key()
    f = Fernet(key)
    with open('C:/Users/acer/PycharmProjects/FuturaLabs/Data_Sharing_In_Cloud_Computing/file/cameo(6-jpeg).jpeg',
              'rb') as original_file:
        orginal = original_file.read()

    encrypted = f.encrypt(orginal)

    with open('file/new.jpeg', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


# encrypt_file()

def decrypt_file():
    key = load_key()
    f = Fernet(key)
    with open('file/new.jpeg', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open('file/dec_new.jpeg', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


decrypt_file()
