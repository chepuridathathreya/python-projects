import threading
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)
server_socket.settimeout(None)
def handling_client(client_socket):
        while True:
            data = client_socket.recv(1024)
            print("Message from client: ", data.decode())
            if data.decode() == "exit":
                break
            # msg = input("Enter message to send to client: ")
            # client_socket.send(msg.encode())

while True:
    client_socket, address = server_socket.accept()
    print("Connection from: ", address)
    thread = threading.Thread(target=handling_client, args=(client_socket,))
    thread.start()