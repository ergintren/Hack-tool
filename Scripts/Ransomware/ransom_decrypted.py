import os
from cryptography.fernet import Fernet

class Decrypt():

    def Decrypt(self):
        file_list = []

        for file in os.listdir():
            if file == "ransom_decrypted.exe" or file == "ransom_decrypted.py":
                continue
            if os.path.isfile(file):
                file_list.append(file)
        secret_key = "1122"

        for file in file_list:
            with open(file,"rb") as the_file:
                contents = the_file.read()
            contents_decrypted = Fernet(secret_key).decrypt(contents)
            with open(file,"wb") as the_file:
                the_file.write(contents_decrypted)

test = Decrypt()
test.Decrypt()