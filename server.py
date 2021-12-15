import socket 
import threading 
from concurrent.futures import ThreadPoolExecutor
import helper 

client_list = []

class ClientHandler:
	def __init__(self, conn, username):
		self.conn = conn 
		self.username = username
		threading.Thread(target=self.run).start()

	def run(self):
		global client_list
		while True:
			message = self.conn.recv(1024)
			message = message.decode('utf-8')
			print(f"{username}> " + message)
			for client in client_list:
				if (client.username != self.username):
					client.display(message, self.username)

	def display(self, message, sender_username):
		message = f"{sender_username}> " + message 
		message = message.encode()
		self.conn.sendall(message)

def handle_client(conn, username):
	while True:
		message = conn.recv(1024)
		message = message.decode('utf-8')
		print(f"{username}> " + message)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((helper.HOST, helper.PORT))
serverSocket.listen()

conn_list = list()

executor = ThreadPoolExecutor(5)

while True:
	conn, addr = serverSocket.accept()
	username = conn.recv(1024).decode('utf-8')
	print(username)
	# I now have an object for the client 
	# Make a thread to handle the client
	# executor.submit(handle_client, conn, username)
	client_list.append(ClientHandler(conn, username))