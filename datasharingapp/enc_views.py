# from cryptography.fernet import Fernet
#
#
# # def write_key():
# #     key = Fernet.generate_key()
# #     with open("key.key", "wb") as key_file:
# #         key_file.write(key)
# #         print("key Generated")
#
#
# def load_key():
#     return open("../key.key", "rb").read()
#
#
# # write_key()
# # key = load_key()
#
#
# # message = "my name is".encode()
# # f = Fernet(key)
# # encrypted = f.encrypt(message)
# # print(encrypted)
# #
# # decrypted_encrypted = f.decrypt(encrypted)
# # print(decrypted_encrypted)
#
#
# def encrypt(filename, key):
#     """
#     Given a filename (str) and key (bytes), it encrypts the file and write it
#     """
#     f = Fernet(key)
#     with open(filename, "rb") as file:
#         # read all file data
#         file_data = file.read()
#     # encrypt data
#     encrypted_data = f.encrypt(file_data)
#
#     # write the encrypted file
#     with open(filename, "wb") as file:
#         file.write(encrypted_data)
#         print("encrypted data", encrypted_data)
#
#
# def decrypt(filename, key):
#     """
#     Given a filename (str) and key (bytes), it decrypts the file and write it
#     """
#     f = Fernet(key)
#     with open(filename, "rb") as file:
#         # read the encrypted data
#         encrypted_data = file.read()
#     # decrypt data
#     decrypted_data = f.decrypt(encrypted_data)
#     # write the original file
#     with open(filename, "wb") as file:
#         file.write(decrypted_data)
#         print("decrypted values are: ", decrypted_data)
#
#
# key = load_key()
# file = "C:/Users/acer/PycharmProjects/FuturaLabs/Data_Sharing_In_Cloud_Computing/datasharingapp/hello/37146944.jpg"
# # encrypt(file, key)
# decrypt(file, key)
