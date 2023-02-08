
import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8000)) #Ip address and port number to connect to

def receive_messages():
    while True:
        message = client.recv(1024).decode() #When a message is recieved, it will be decoded (it is encoded in server)
        if not message:
            break
        print(f"Received message: {message}")

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input("Enter a message: ")
    client.sendall(message.encode())
