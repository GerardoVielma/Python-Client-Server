#!/bin/python3

import socket 
import threading

HEADER = 64
PORT = 8888
SERVER = socket.gethostbyname(socket.gethostname())#retrieves ip address of laptop/host 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Socket defines connection between server and client. AF_INET is the category of socket like IPv4.  Sockstream streams the data to socket.

server.bind(ADDR)#Binds the socket to the server address

#uses conn to be able to communicate back to the client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
	#while the client is connected, the loop continuous 
    connected = True
    while connected:
    #HEADER is the actual length of the message coming from client. Decode is needed to change the byte format to string.
    #conn is socket object, msg_length is now string
        msg_length = conn.recv(HEADER).decode(FORMAT)
        #msg_length checks to see if the input is empty or not.
        if msg_length:
            msg_length = int(msg_length)
            #Recieves the msg
            #make sure recv is large enough to contain all the message
            msg = conn.recv(msg_length).decode(FORMAT)
            
           #Caps the string recieved from client.
            caps = msg.upper()
            #If client wants to disconnect
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
			#Prints the address of the client and message
            print(f"Received: {msg}")
            #Every time the server recieves a message from client, it sends caps to client
            print("Sent to client:", end = ' ')
            print(caps)
            conn.send(caps.encode(FORMAT)) #Replace this with the translated message.

	#Cleanly disconnects client from server, they can join again if they want.
    conn.close()
        
#Listens to clients and handles them, might need to change this to echo or something
def start():
    server.listen()
    print(f"Connected from {SERVER}, port {PORT}")
    #Server listens forever
    while True:
    	#Server waits(blocks) until a new connection has been made. Conn is a socket object that allows us to communicate with the client. addr is the address from the client (IP)
        conn, addr = server.accept()
        #Each client will go in a thread because we dont want to wait for a client to finish before starting another.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("Waiting for incoming connection")
#Start the server
start()
