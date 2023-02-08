
import socket
import threading

clients = [] #Users who use this application

def handle_client(client_socket, client_address):
    clients.append(client_socket)
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        for myself in clients: #myself is referred to the specific user, so long his not sending messages to himself, others will recieve it
            if myself != client_socket:
                myself.sendall(f"{client_address}: {message.decode()}".encode()) #This is so that other users will see his message instead of only him writing to himself
    clients.remove(client_socket)
    client_socket.close()


#clients.remove(client_socket) and client_socket.close()
#are used to handle the closing of a client connection. clients.remove(client_socket)
#removes the client socket from the list of connected clients,
#while client_socket.close() closes the socket, freeing up system resources and ending the connection with the client.

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8000)) #The ip address and port in which this application is used with
server_socket.listen(5)

print("Listening on port 8000")

while True: #When client_socket and adress is connected to the server_socket, it will print which clients have connected
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address)) #Needed to take start the handle_client function
    client_thread.start()
