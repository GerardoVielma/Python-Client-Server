#!/bin/python3

import socket

HEADER = 64
PORT = 8888
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#The IP address of the server that the client will connect to (it's the local IP address of your computer because you created the server on this computer.
SERVER = input('Enter IP address:')#socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)#Tupple that contains the server address and the port

#create socket for client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#instead of bind(), connect() to the address server. ADDR contains server address and port
client.connect(ADDR)

#Function that sends message from client to server.
def send(msg):
	#encodes the Hello World! message from string to byte format using format 'utf-8'
    message = msg.encode(FORMAT)
    #FIRST message sent to server is the length of the message
    msg_length = len(message)
    #'msg_length' is a int variable turned into string, then encoded to byte format
    send_length = str(msg_length).encode(FORMAT)
    #Send_lenght must be equal to HEADER(64), so we pad white spaces until it becomes equal. b means byte format
    send_length += b' ' * (HEADER - len(send_length))
    #Sends send_length to server, then sends the actual message. This send is different because it is using the socket client.
    client.send(send_length)
    client.send(message)
    print(msg)
    
    #Recieves the length of the message sent from the server to the client.(2048 is a very large number because we do not know the length of the actual message the server will send.
    print("Server sent:" , end = ' ')
    print(client.recv(2048).decode(FORMAT))

#For the project, make a while loop that the client keeps sending strings
while True:
	send("abcdef")
	input()#Waiting for Enter or any input
	send("123")
	input()
	send("have a great day!")
	#send(DISCONNECT_MESSAGE)
