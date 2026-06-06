import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))
while True:
    message = input("Enter message to send to server: ")
    client_socket.send(message.encode())
    if message == "exit":
        break
    data = client_socket.recv(1024)
    print("Message from server: ", data.decode())