import socket 
import threading 
import helper 

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((helper.HOST, helper.PORT))

username = input("Enter your username: ").strip().encode()
clientSocket.sendall(username)

def message_displayer():
	global clientSocket
	while True:
		message = clientSocket.recv(1024).decode('utf-8')
		print('\r      \r', end='')
		print(message + '\n> ', end='')

threading.Thread(target=message_displayer).start()

while True:
	message = input('\r      \r> ').strip().encode()
	if message is None:
		continue
	clientSocket.sendall(message)